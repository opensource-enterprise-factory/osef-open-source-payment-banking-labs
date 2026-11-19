#!/usr/bin/env bash
# OSEF FRAUD-002 — Tests Tazama Public DockerHub via collection Newman OFFICIELLE.
# Source externe synchronisée via Git (jamais de modification des fichiers sur la VM).
# Réalise des écritures de transactions synthétiques dans Tazama ; ne pas utiliser en production.
set -euo pipefail

OSEF_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
POSTMAN_DIR="${TAZAMA_POSTMAN_DIR:-/home/lionel/tazama-postman}"
COLLECTION='Newman/Newman - 2.1. (NO-AUTH) Public DockerHub End-to-End Test.postman_collection.json'
ENV_FILE='environments/Tazama-Docker-Compose.postman_environment.json'

if [[ ! -f "$POSTMAN_DIR/$COLLECTION" || ! -f "$POSTMAN_DIR/$ENV_FILE" ]]; then
  echo "[BLOCK] Collection officielle introuvable dans $POSTMAN_DIR" >&2
  echo "Synchroniser la source upstream : git clone https://github.com/tazama-lf/postman.git '$POSTMAN_DIR'" >&2
  exit 2
fi

# Le contrôle ne redémarre aucun service et garantit que l'overlay de sécurité est en place.
python3 "$OSEF_REPO/labs/FRAUD-002/scripts/tazama-safe.py" check
for endpoint in 'http://127.0.0.1:5000/' 'http://127.0.0.1:5100/'; do
  code="$(curl -sS -o /dev/null -w '%{http_code}' --max-time 8 "$endpoint")" || {
    echo "[BLOCK] API indisponible: $endpoint" >&2
    exit 2
  }
  if [[ "$code" != 200 ]]; then
    echo "[BLOCK] API $endpoint renvoie HTTP $code (200 attendu)" >&2
    exit 2
  fi
  echo "[OK] $endpoint HTTP 200"
done

# Split the unchanged upstream collection into its two official folders.
# Phase 1 generates NEW synthetic messages, runs their API POSTs and exports
# Newman globals. Between phases, a bounded GET-only poll waits for the exact
# pacs.002 Admin report. Phase 2 runs ALL original upstream assertions.
# Neither the report nor a modified collection is ever written to disk.
echo "[INFO] Phase 1/2 : création et soumission des messages synthétiques."
echo "[INFO] Aucun port exposé : Newman en réseau host dans la VM Ubuntu."
WORK_DIR="$(mktemp -d "${TMPDIR:-/tmp}/osef-newman.XXXXXXXX")"
chmod 700 "$WORK_DIR"
trap 'rm -rf -- "$WORK_DIR"' EXIT
GLOBALS_PATH="$WORK_DIR/globals.json"

docker run --rm --network host \
  --user "$(id -u):$(id -g)" \
  --mount "type=bind,src=$POSTMAN_DIR,dst=/etc/newman,readonly" \
  --mount "type=bind,src=$WORK_DIR,dst=/osef-work" \
  postman/newman:alpine \
  run "/etc/newman/$COLLECTION" \
  -e "/etc/newman/$ENV_FILE" \
  --folder "Message Creation sans pain.001/013" \
  --export-globals /osef-work/globals.json \
  --timeout-request 10200 \
  --delay-request 500

if [[ ! -s "$GLOBALS_PATH" ]]; then
  echo "[BLOCK] Newman n'a pas exporté les variables de phase 1." >&2
  exit 2
fi

echo "[INFO] Attente bornée du rapport Admin (GET seulement, maximum 30 essais / 2 s)."
python3 "$OSEF_REPO/labs/FRAUD-002/scripts/wait-tazama-newman-report.py" \
  --globals "$GLOBALS_PATH" --attempts 30 --interval 2

echo "[INFO] Phase 2/2 : assertions officielles Admin sur le même rapport."
docker run --rm --network host \
  --user "$(id -u):$(id -g)" \
  --mount "type=bind,src=$POSTMAN_DIR,dst=/etc/newman,readonly" \
  --mount "type=bind,src=$WORK_DIR,dst=/osef-work,readonly" \
  postman/newman:alpine \
  run "/etc/newman/$COLLECTION" \
  -e "/etc/newman/$ENV_FILE" \
  --folder "DB update tests" \
  --globals /osef-work/globals.json \
  --timeout-request 10200

echo "[OK] Deux phases Newman terminées : assertions officielles validées."
