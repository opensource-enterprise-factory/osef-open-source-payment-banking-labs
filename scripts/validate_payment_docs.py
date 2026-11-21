#!/usr/bin/env python3
"""Validate OSEF payment documentation and 75-lab catalogue, using Python stdlib."""
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ACADEMY = ROOT / "docs/academy/payment-engineer"
ROADMAP = ROOT / "docs/roadmap"
VEILLE = ROOT / "veille/2026/2026-11-21"
FILES = (
    sorted(ACADEMY.glob("*.md"))
    + sorted(ROADMAP.glob("*.md"))
    + sorted((ROADMAP / "pilot-L1-L2").glob("*.md"))
    + sorted(VEILLE.glob("*.md"))
    + sorted((VEILLE / "labs").glob("*.md"))
    + sorted((VEILLE / "meetups").glob("*.md"))
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
errors = []

for document in FILES:
    content = document.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(content):
        raw = match.group(1).strip()
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = unquote(raw.split("#", 1)[0])
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        resolved = document.parent / target
        if not resolved.is_file():
            errors.append(f"{document.relative_to(ROOT)}: missing relative link {raw}")

basename = "OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21"
csv_path = ROADMAP / (basename + ".csv")
json_path = ROADMAP / (basename + ".json")
with csv_path.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
with json_path.open(encoding="utf-8") as f:
    obj = json.load(f)
labs = obj.get("labs", [])
if len(rows) != len(labs) or len(rows) != obj.get("count"):
    errors.append(f"catalogue mismatch: csv={len(rows)}, json={len(labs)}, declared={obj.get('count')}")
if len(rows) != 75:
    errors.append(f"catalogue expected 75 entries; received {len(rows)}")
ids_csv = [r["id"] for r in rows]
ids_json = [r["id"] for r in labs]
if len(ids_csv) != len(set(ids_csv)):
    errors.append("duplicate lab ID in CSV")
if ids_csv != ids_json:
    errors.append("JSON and CSV lab ID order or contents differ")

print(f"Validated {len(FILES)} Markdown files and {len(rows)} catalogue rows.")
if errors:
    print("\n".join("ERROR: " + err for err in errors), file=sys.stderr)
    sys.exit(1)
print("OK: local links and catalogue structure consistent.")
