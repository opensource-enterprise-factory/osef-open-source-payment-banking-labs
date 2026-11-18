#!/usr/bin/env bash
# Génère quatre clés aléatoires de démonstration sans écraser une configuration existante.
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ -e .env ]]; then
  echo ".env existe : aucune clé remplacée. Sauvegardez-le si nécessaire." >&2
  exit 0
fi
command -v openssl >/dev/null || { echo "Installez openssl."; exit 1; }
umask 077
{
  echo "LAB_USER_KEY=$(openssl rand -hex 24)"
  echo "PSP_A_KEY=$(openssl rand -hex 24)"
  echo "PSP_B_KEY=$(openssl rand -hex 24)"
  echo "ADMIN_KEY=$(openssl rand -hex 24)"
} > .env
echo "Clés de lab générées dans .env (ne pas committer)."
