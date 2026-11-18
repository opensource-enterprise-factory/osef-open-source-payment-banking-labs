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

echo "[INFO] Exécution de transactions synthétiques via TMS puis lecture du rapport Admin."
echo "[INFO] Aucune exposition réseau : conteneur Newman en mode host sur Ubuntu uniquement."
docker run --rm --network host \
  --mount "type=bind,src=$POSTMAN_DIR,dst=/etc/newman,readonly" \
  postman/newman:alpine \
  run "/etc/newman/$COLLECTION" \
  -e "/etc/newman/$ENV_FILE" \
  --timeout-request 10200 \
  --delay-request 500
