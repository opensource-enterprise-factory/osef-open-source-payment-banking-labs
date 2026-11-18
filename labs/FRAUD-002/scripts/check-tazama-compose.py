#!/usr/bin/env python3
"""FRAUD-002 - Read-only Tazama Compose publication and resource audit.

Only synthetic lab use. Does not create files, containers, volumes, or run up/down.
Uses official Tazama Public (DockerHub) compose file selection, same as menu option 2,
without optional addons. Does not print environment variables or secrets.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

FILES = (
    "docker-compose.base.infrastructure.yaml",
    "docker-compose.base.override.yaml",
    "docker-compose.hub.cfg.yaml",
    "docker-compose.hub.core.yaml",
    "docker-compose.hub.rules.yaml",
)
FRAUD_PORTS = {8090, 8091, 8092}


def main() -> int:
    base = Path(os.environ.get("TAZAMA_CORE_DIR", "/home/lionel/tazama-stack/core"))
    if not base.is_dir():
        print(f"[ERROR] Répertoire Tazama introuvable : {base}", file=sys.stderr)
        return 2
    missing = [name for name in FILES if not (base / name).is_file()]
    if missing:
        print(f"[ERROR] Fichiers Compose absents : {', '.join(missing)}", file=sys.stderr)
        return 2

    command = ["docker", "compose"]
    for filename in FILES:
        command.extend(("-f", filename))
    command += ["config", "--format", "json"]

    try:
        completed = subprocess.run(
            command, cwd=base, check=False, capture_output=True, text=True,
        )
    except OSError as exc:
        print(f"[ERROR] Docker Compose indisponible : {exc}", file=sys.stderr)
        return 2

    if completed.returncode:
        print("[ERROR] La configuration Compose ne peut pas être validée.", file=sys.stderr)
        print(
            "Vérifier les fichiers .env et les dépendances selon le README officiel ; "
            "la sortie d'erreur de Compose n'est pas reproduite pour éviter une fuite de secrets.",
            file=sys.stderr,
        )
        return 2

    try:
        data = json.loads(completed.stdout)
        services = data["services"]
    except (ValueError, KeyError, TypeError):
        print("[ERROR] Réponse Compose JSON illisible.", file=sys.stderr)
        return 2

    conflicts = []
    externally_published = []
    print("FRAUD-002 : audit lecture seule des publications de ports")
    print(f"Répertoire Tazama : {base}")
    print(f"Nombre de services : {len(services)}")
    for name, service in services.items():
        ports = service.get("ports") or []
        memory = ((service.get("deploy") or {}).get("resources") or {}).get("limits", {}).get("memory", "non défini")
        if not ports:
            print(f"  {name}: ports publiés = aucun ; limite RAM = {memory}")
            continue
        labels = []
        for port in ports:
            try:
                host_port = int(port.get("published", 0))
            except (ValueError, TypeError):
                host_port = 0
            host_ip = port.get("host_ip") or "0.0.0.0 (par défaut)"
            target = port.get("target", "?")
            labels.append(f"{host_ip}:{host_port or '?'} -> {target}")
            if host_port in FRAUD_PORTS:
                conflicts.append((name, host_port))
            if host_ip in ("0.0.0.0", "::", "0.0.0.0 (par défaut)"):
                externally_published.append((name, host_port))
        print(f"  {name}: {', '.join(labels)} ; limite RAM = {memory}")

    if conflicts:
        print("[FAIL] Conflits potentiels avec FRAUD-001 :")
        for name, port in conflicts:
            print(f"  - {name}: {port}")
    else:
        print("[OK] Aucun port publié commun à 8090, 8091, 8092 dans ce profil.")

    if externally_published:
        print("[WARN] Publications sans liaison exclusive explicite à localhost :")
        for name, port in externally_published:
            print(f"  - {name}: {port or 'port indéterminé'}")
        print(
            "Les interfaces 0.0.0.0/:: peuvent être exposées sur plusieurs cartes "
            "de la VM ; prévoir une configuration de restriction revue par PR "
            "avant de lancer Tazama."
        )
    else:
        print("[OK] Aucune publication non restreinte identifiée.")
    print("Aucun conteneur ni fichier n'a été modifié.")
    return 1 if conflicts or externally_published else 0


if __name__ == "__main__":
    raise SystemExit(main())
