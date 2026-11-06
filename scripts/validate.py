"""Validate data/data.yaml against data/schema.json plus cross-field rules.

Usage: python3 scripts/validate.py [path/to/data.yaml]
Exits 1 on any error. Run via `make check`.
"""

import json
import sys
from datetime import date
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent


def date_floor(s: str) -> date:
    """Earliest day a (possibly partial) date could mean."""
    parts = [int(p) for p in s.split("-")]
    return date(
        parts[0], parts[1] if len(parts) > 1 else 1, parts[2] if len(parts) > 2 else 1
    )


def validate(
    data_path: Path, schema_path: Path, metadata_path: Path | None = None
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    data = yaml.safe_load(data_path.read_text())
    schema = json.loads(schema_path.read_text())

    for err in sorted(
        Draft202012Validator(schema).iter_errors(data),
        key=lambda e: list(e.absolute_path),
    ):
        path = "/".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"{path}: {err.message}")
    if errors:  # cross-field rules assume a well-formed file
        return errors, warnings

    entries = [(sec, e) for sec, items in data.items() for e in items]
    names = {e["name"] for _, e in entries}
    seen: dict[str, str] = {}
    metadata = {}
    if metadata_path and metadata_path.exists():
        metadata = yaml.safe_load(metadata_path.read_text()) or {}
    today = date.today()

    for sec, e in entries:
        where = f"{sec}/{e['name']}"
        if e["link"] in seen:
            errors.append(f"{where}: link also used by {seen[e['link']]}")
        seen[e["link"]] = where
        if "superseded_by" in e and e["superseded_by"] not in names:
            errors.append(
                f"{where}: superseded_by {e['superseded_by']!r} is not an entry name"
            )
        if "released" in e:
            floor = date_floor(e["released"])
            if floor > today:
                errors.append(f"{where}: released {e['released']} is in the future")
            created = (metadata.get(e["link"]) or {}).get("created")
            # A release can't predate its own repo. Slack for partial dates and repos
            # that were migrated/renamed, so only flag clear contradictions (>31 days).
            if created and (date.fromisoformat(created[:10]) - floor).days > 31:
                warnings.append(
                    f"{where}: released {e['released']} is before the repo's creation date "
                    f"{created[:10]} (fine if the product predates this repo, otherwise check the source)"
                )
    return errors, warnings


def main() -> int:
    data_path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "data.yaml"
    errors, warnings = validate(
        data_path, ROOT / "data" / "schema.json", ROOT / "data" / "metadata.yaml"
    )
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"{len(errors)} error(s)" if errors else "data.yaml OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
