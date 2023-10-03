import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime, timedelta

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("README.md.in")

with open("data/data.yaml", "r") as f:
    tables = yaml.safe_load(f)

with open("data/metadata.yaml", "r") as f:
    metadata = yaml.safe_load(f)

# combine
for cat in tables:
    for row in tables[cat]:
        if row["link"] in metadata:
            data = metadata[row["link"]]
            if "stars" in data:
                row["stars"] = data["stars"]
            if "released" in data:
                row["released"] = datetime.strptime(
                    data["released"][:10], "%Y-%m-%d"
                ).date()

# determine which are "new" (released in the last 30 days)
cutoff = datetime.now() - timedelta(days=30)
for cat in tables:
    for row in tables[cat]:
        if "released" in row and isinstance(row["released"], datetime):
            row["new"] = row["released"] > cutoff


rendered_template = template.render(tables)

with open("README.md", "w") as f:
    f.write(rendered_template)
print("README.md generated")
