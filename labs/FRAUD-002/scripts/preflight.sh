#!/usr/bin/env bash
# OSEF FRAUD-002 — vérifications non destructives avant Tazama Core sur Ubuntu.
# Ne démarre ni ne modifie Docker, et n'affiche aucun secret.
set -uo pipefail
ERRORS=0
WARNINGS=0
info() { printf '[INFO] %s\n' "$*"; }
warn() { printf '[WARN] %s\n' "$*"; WARNINGS=$((WARNINGS+1)); }
fail() { printf '[FAIL] %s\n' "$*"; ERRORS=$((ERRORS+1)); }
ok() { printf '[OK] %s\n' "$*"; }
info "Pré-contrôle Tazama / Ubuntu, sans installation."
if [[ "$(uname -s)" != "Linux" ]]; then
  warn "Ce guide vise Ubuntu Linux (OS détecté : $(uname -s))."
fi
if [[ -r /etc/os-release ]]; then
  . /etc/os-release
  info "Système: ${PRETTY_NAME:-Linux}"
else
  warn "Impossible de lire /etc/os-release."
fi
if command -v git >/dev/null 2>&1; then
  ok "Git: $(git --version)"
else fail "git absent"; fi
if command -v curl >/dev/null 2>&1; then
  ok "curl installé"
else fail "curl absent"; fi
if command -v docker >/dev/null 2>&1; then
  ok "Docker CLI: $(docker --version)"
  if docker info >/dev/null 2>&1; then
    ok "Docker Engine accessible par l'utilisateur courant."
    DOCKER=(docker)
  elif command -v sudo >/dev/null 2>&1 && sudo -n docker info >/dev/null 2>&1; then
    ok "Docker Engine accessible via sudo (sans invite)."
    DOCKER=(sudo docker)
  else
    warn "Docker Engine inaccessible à l'utilisateur courant. Réessayer via sudo docker après authentification ; ne pas donner de permissions larges au socket."
    DOCKER=(docker)
  fi
  if "${DOCKER[@]}" compose version >/dev/null 2>&1; then
    ok "Docker Compose: $("${DOCKER[@]}" compose version)"
  else
    fail "Docker Compose v2 non détecté (ou droits insuffisants)."
  fi
else
  fail "Docker CLI absent."
fi
if command -v free >/dev/null 2>&1; then
  free -h
fi
if command -v df >/dev/null 2>&1; then
  df -h .
fi
if command -v nproc >/dev/null 2>&1; then
  info "vCPU visibles: $(nproc)"
fi
if command -v ss >/dev/null 2>&1; then
  # Port utilisé par la version documentée de la pile ; pas un inventaire exhaustif.
  info "Ports TCP écoutés sur la VM (vérifier les conflits avant installation):"
  ss -ltn | head -n 30
else
  warn "ss indisponible, impossible d'inspecter les ports."
fi
if [[ -d ./tazama-stack/.git ]]; then
  info "Dépôt Tazama déjà présent, commit: $(git -C ./tazama-stack rev-parse --short HEAD 2>/dev/null || echo inconnu)"
else
  info "Dépôt tazama-stack non cloné dans le dossier courant."
fi
info "Cette vérification ne mesure pas la capacité nécessaire à Tazama et n'établit aucune compatibilité."
info "Résumé: $ERRORS erreur(s) bloquante(s) et $WARNINGS avertissement(s)."
(( ERRORS == 0 )) || exit 1
