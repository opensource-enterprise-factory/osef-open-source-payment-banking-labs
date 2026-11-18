#!/usr/bin/env bash
# Test de bout en bout : requiert Docker Compose démarré, curl et Python 3 local.
set -euo pipefail
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
    curl --silent --show-error --output "$TMP/result.json" --write-out '%{http_code}' \
      --request "$method" --header "X-Lab-Key: $key" --header 'Content-Type: application/json' --data-binary "@$file" "$url"
  else
    curl --silent --show-error --output "$TMP/result.json" --write-out '%{http_code}' \
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
status=$(curl --silent --show-error --output "$TMP/result.json" --write-out '%{http_code}' http://127.0.0.1:8090/signals); assert_status 401 "$status" "lecture relay sans autorisation"
status=$(curl --silent --show-error --output "$TMP/result.json" --write-out '%{http_code}' -H "X-API-Key: $ADMIN_KEY" http://127.0.0.1:8090/audit); assert_status 200 "$status" "journal d'audit"
python3 -c 'import json,sys; data=json.load(open(sys.argv[1])); assert len(data["events"])>0; print("OK audit non vide")' "$TMP/result.json"
echo "Tests du périmètre minimum terminés. La purge TTL, la charge et la tolérance aux pannes demandent des tests complémentaires."
