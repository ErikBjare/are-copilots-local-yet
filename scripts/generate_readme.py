"""Render README.md from data/data.yaml + data/metadata.yaml. Offline and deterministic:
"today" is the newest fetched_at in the metadata, not the wall clock."""

from datetime import date
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

from status import compute_status

ROOT = Path(__file__).resolve().parent.parent
tables = yaml.safe_load((ROOT / "data" / "data.yaml").read_text())
metadata = yaml.safe_load((ROOT / "data" / "metadata.yaml").read_text()) or {}

fetched = [m["fetched_at"][:10] for m in metadata.values() if m.get("fetched_at")]
as_of = date.fromisoformat(max(fetched)) if fetched else date.today()

for cat, rows in tables.items():
    for row in rows:
        meta = metadata.get(row["link"], {})
        if "stars" in meta:
            row["stars"] = meta["stars"]
        row["last_activity"] = (meta.get("pushed_at") or "")[:7]
        row["status"] = compute_status(cat, row, meta, as_of)

env = Environment(loader=FileSystemLoader(ROOT))
template = env.get_template("README.md.in")
rendered = template.render({k.replace("-", "_"): v for k, v in tables.items()})
(ROOT / "README.md").write_text(rendered)
print("README.md generated")
