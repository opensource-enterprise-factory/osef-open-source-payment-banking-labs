#!/usr/bin/env python3
"""OSEF FRAUD-002: validate and run versioned Tazama Core safely.

Actions: check (no changes), up (starts Tazama), ps (status), logs (recent logs).
Never performs down, prune, volume deletion or modifies Tazama upstream files.
Only lab synthetic data. Requires Docker Compose support for !override.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

CORE = Path(os.environ.get("TAZAMA_CORE_DIR", "/home/lionel/tazama-stack/core"))
OVERLAY = Path(__file__).resolve().parents[1] / "compose.loopback.yaml"
FILES = [
    "docker-compose.base.infrastructure.yaml",
    "docker-compose.base.override.yaml",
    "docker-compose.hub.cfg.yaml",
    "docker-compose.hub.core.yaml",
    "docker-compose.hub.rules.yaml",
]
DEMO_HOST_IP = "192.168.255.10"  # Réseau privé VirtualBox, pas une adresse publique.
EXPECTED = {
    ("admin-service", 5100), ("batch-ppa", 4100), ("core-postgres", 15432),
    ("nats", 14222), ("nats", 16222), ("nats", 18222),
    ("tazama-demo", 3011), ("tms-service", 5000), ("valkey", 16379),
}


def main():
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in ("check", "up", "ps", "logs"):
        print("Usage: python3 scripts/tazama-safe.py check|up|ps|logs")
        return 2
    if not CORE.is_dir() or not OVERLAY.is_file() or any(not (CORE / f).is_file() for f in FILES):
        print("[ERROR] Clone Tazama ou overlay OSEF introuvable.", file=sys.stderr)
        return 2

    cmd = ["docker", "compose", "-p", "tazama-core"]
    for file in FILES:
        cmd += ["-f", str(CORE / file)]
    cmd += ["-f", str(OVERLAY)]

    result = subprocess.run(cmd + ["config", "--format", "json"], cwd=CORE, capture_output=True, text=True)
    if result.returncode:
        print(
            "[ERROR] Compose config a échoué. Vérifier la version Compose, les fichiers .env "
            "et la syntaxe !override. Détails masqués par précaution contre la fuite de secrets.",
            file=sys.stderr,
        )
        return 2
    try:
        services = json.loads(result.stdout)["services"]
        published = set()
        for name, service in services.items():
            for port in service.get("ports", []):
                host = port.get("host_ip")
                number = int(port["published"])
                expected_ip = DEMO_HOST_IP if (name, number) == ("tazama-demo", 3011) else "127.0.0.1"
                if host != expected_ip:
                    raise ValueError(f"{name} publie {number} sur {host!r}, attendu {expected_ip!r}")
                if number in (8090, 8091, 8092):
                    raise ValueError(f"{name} utilise le port FRAUD-001 {number}")
                published.add((name, number))
        if published != EXPECTED:
            raise ValueError(f"Publications divergentes (attendu {len(EXPECTED)}, observé {len(published)}).")
        if len(services) != 13:
            raise ValueError(f"Nombre de services inattendu : {len(services)} au lieu de 13.")
    except (ValueError, KeyError, TypeError) as e:
        print(f"[BLOCK] Déploiement interdit : {e}", file=sys.stderr)
        return 1

    print("[OK] 13 services, 8 ports localhost et Tazama Demo sur 192.168.255.10:3011 ; aucune collision 8090–8092.")
    print("[INFO] Aucune limite mémoire déclarée ; ne lancer 'up' qu'après validation des ressources et du disque.")
    if action == "check":
        print("[INFO] Contrôle en lecture seule, aucun conteneur démarré.")
        return 0
    if action == "up":
        print("[INFO] Démarrage Tazama Core via profil Public (DockerHub) + overlay OSEF.")
        args = ["up", "-d"]  # pas de --remove-orphans, --force-recreate ou --volumes
    elif action == "ps":
        args = ["ps"]
    else:
        args = ["logs", "--tail", "80", "tms-service", "event-director", "event-adjudicator"]
    return subprocess.run(cmd + args, cwd=CORE, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
