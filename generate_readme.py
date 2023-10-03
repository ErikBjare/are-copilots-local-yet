import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("README.md.in")

with open("data.yaml", "r") as f:
    tables = yaml.safe_load(f)

with open("stars.yaml", "r") as f:
    stars = yaml.safe_load(f)

# combine
for cat in tables:
    for row in tables[cat]:
        print(stars, row["link"])
        if row["link"] in stars:
            row["stars"] = stars[row["link"]]["stars"]


rendered_template = template.render(tables, stars=stars)

with open("README.md", "w") as f:
    f.write(rendered_template)
print("README.md generated")
