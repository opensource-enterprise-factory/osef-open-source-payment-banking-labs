#!/usr/bin/env bash
# Test de bout en bout : requiert Docker Compose démarré, curl et Python 3 local.
set -euo pipefail
if [[ $# -gt 1 || ( $# -eq 1 && "$1" != "--extended" ) ]]; then
  echo "Usage: bash scripts/test-lab.sh [--extended]" >&2
  exit 2
fi
cd "$(dirname "$0")/.."
[[ -f .env ]] || { echo "Exécuter d'abord bash scripts/init-env.sh"; exit 1; }
set -a; source .env; set +a
command -v curl >/dev/null || { echo "curl manquant"; exit 1; }
command -v python3 >/dev/null || { echo "python3 manquant"; exit 1; }
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
TOKEN="demo-$(date +%s)-$$"
cat > "$TMP/valid.json" <<JSON
{"transaction_token":"$TOKEN","category":"suspicious-transfer","severity":"high","recipient":"psp-b","expires_in_hours":1}
JSON
request() { # URI method payload? header? => imprime le statut HTTP ; le JSON est dans $TMP/result.json
  local url="$1" method="$2" key="$3" file="${4:-}"
  if [[ -n "$file" ]]; then
    curl --silent --show-error --max-time 15 --output "$TMP/result.json" --write-out '%{http_code}' \
      --request "$method" --header "X-Lab-Key: $key" --header 'Content-Type: application/json' --data-binary "@$file" "$url"
  else
    curl --silent --show-error --max-time 15 --output "$TMP/result.json" --write-out '%{http_code}' \
      --request "$method" --header "X-Lab-Key: $key" "$url"
  fi
}
assert_status() { local expected="$1" actual="$2" name="$3"; [[ "$expected" == "$actual" ]] || { echo "ÉCHEC $name : attendu $expected, obtenu $actual"; cat "$TMP/result.json"; exit 1; }; echo "OK $name ($actual)"; }
status=$(request http://127.0.0.1:8091/submit POST "$LAB_USER_KEY" "$TMP/valid.json"); assert_status 201 "$status" "signal accepté"
status=$(request http://127.0.0.1:8091/submit POST "$LAB_USER_KEY" "$TMP/valid.json"); assert_status 409 "$status" "idempotence : doublon rejeté"
status=$(request http://127.0.0.1:8091/submit POST invalid "$TMP/valid.json"); assert_status 401 "$status" "clé client invalide"
status=$(request http://127.0.0.1:8092/inbox GET "$LAB_USER_KEY"); assert_status 200 "$status" "lecture PSP B"
python3 -c 'import json,sys; data=json.load(open(sys.argv[1])); token=sys.argv[2]; assert any(x["transaction_token"]==token for x in data["signals"]), "Signal absent"; print("OK signal retrouvé côté PSP B")' "$TMP/result.json" "$TOKEN"
echo '{"transaction_token":"demo-invalid77","category":"bad-category","severity":"high","recipient":"psp-b","expires_in_hours":1}' > "$TMP/invalid.json"
status=$(request http://127.0.0.1:8091/submit POST "$LAB_USER_KEY" "$TMP/invalid.json"); assert_status 422 "$status" "schéma invalide"
status=$(curl --silent --show-error --max-time 15 --output "$TMP/result.json" --write-out '%{http_code}' http://127.0.0.1:8090/signals); assert_status 401 "$status" "lecture relay sans autorisation"
status=$(curl --silent --show-error --max-time 15 --output "$TMP/result.json" --write-out '%{http_code}' -H "X-API-Key: $ADMIN_KEY" http://127.0.0.1:8090/audit); assert_status 200 "$status" "journal d'audit"
python3 -c 'import json,sys; data=json.load(open(sys.argv[1])); assert len(data["events"])>0; print("OK audit non vide")' "$TMP/result.json"
echo "Tests du périmètre minimum terminés. La purge TTL, la charge et la tolérance aux pannes demandent des tests complémentaires."

[[ ${1:-} == "--extended" ]] || exit 0

assert_token_visibility() {
  python3 - "$TMP/result.json" "$TOKEN" "$1" <<'PY'
import json
import sys

path, token, expected = sys.argv[1:]
with open(path, encoding="utf-8") as response:
    signals = json.load(response)["signals"]
found = any(signal["transaction_token"] == token for signal in signals)
if found != (expected == "present"):
    sys.exit(f"ÉCHEC : jeton de ce test attendu {expected}")
print(f"OK jeton de ce test : {expected}")
PY
}

# T10 — Contrôle de la séparation des droits d'émission et de lecture.
status=$(curl -sS --max-time 15 -o "$TMP/result.json" -w '%{http_code}' \
  -H "X-API-Key: $PSP_A_KEY" http://127.0.0.1:8090/signals)
assert_status 401 "$status" "T10 : lecture refusée au PSP A"

# T09 — Le relais doit redémarrer même si une assertion échoue.
(
  trap 'result=$?; docker compose start relay || result=1; exit "$result"' EXIT
  trap 'exit 130' INT
  trap 'exit 143' TERM
  docker compose stop relay
  status=$(request http://127.0.0.1:8092/inbox GET "$LAB_USER_KEY")
  assert_status 503 "$status" "T09 : relais arrêté"
  python3 - "$TMP/result.json" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as response:
    if json.load(response).get("detail") != "Lab relay unavailable":
        sys.exit("ÉCHEC T09 : message d’indisponibilité inattendu")
PY
)

ready=0
for (( attempt=0; attempt<30; attempt++ )); do
  if curl -fs --max-time 2 http://127.0.0.1:8090/health > /dev/null; then
    ready=1
    break
  fi
  sleep 1
done
if (( ! ready )); then
  echo "ÉCHEC T09 : le relais ne répond pas après redémarrage" >&2
  exit 1
fi
status=$(request http://127.0.0.1:8092/inbox GET "$LAB_USER_KEY")
assert_status 200 "$status" "T09 : lecture rétablie"
assert_token_visibility present

# T08 — Modifier uniquement l'expiration du signal fictif créé par ce test.
docker compose exec -T relay python - "$TOKEN" <<'PY'
import os
import sqlite3
import sys
from datetime import datetime, timedelta, timezone

expired_at = (datetime.now(timezone.utc) - timedelta(minutes=1)).isoformat()
with sqlite3.connect(os.environ["DATABASE_PATH"]) as db:
    updated = db.execute(
        "UPDATE signals SET expires_at = ? WHERE token = ?",
        (expired_at, sys.argv[1]),
    )
    if updated.rowcount != 1:
        sys.exit("ÉCHEC T08 : signal de test introuvable")
PY
status=$(request http://127.0.0.1:8092/inbox GET "$LAB_USER_KEY")
assert_status 200 "$status" "T08 : lecture après expiration"
assert_token_visibility absent

echo "OK : scénarios T01 à T10 terminés."
