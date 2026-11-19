"""Inspect or purge expired synthetic signals from the FRAUD-001 relay."""
import argparse
import os
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Delete eligible rows")
    args = parser.parse_args()
    if os.environ.get("ROLE") != "relay":
        parser.error("Run this command in the FRAUD-001 relay container")

    database = Path(os.environ["DATABASE_PATH"]).resolve()
    mode = "rw" if args.apply else "ro"
    cutoff = datetime.now(timezone.utc).isoformat()
    eligibility = "expires_at <= ? AND substr(token, 1, 5) = 'demo-'"

    with closing(sqlite3.connect(f"{database.as_uri()}?mode={mode}", uri=True)) as db:
        if args.apply:
            with db:
                result = db.execute(f"DELETE FROM signals WHERE {eligibility}", (cutoff,))
                count = result.rowcount
            print(f"Signaux fictifs expirés supprimés : {count}")
        else:
            count = db.execute(
                f"SELECT count(*) FROM signals WHERE {eligibility}", (cutoff,)
            ).fetchone()[0]
            print(f"Simulation — signaux fictifs expirés éligibles : {count}")


if __name__ == "__main__":
    main()
