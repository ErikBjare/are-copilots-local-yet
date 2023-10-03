import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("README.md.in")

with open("data.yaml", "r") as f:
    tables = yaml.safe_load(f)

# print(f"Tables: {tables.keys()}")

rendered_template = template.render(tables)

with open("README.md", "w") as f:
    f.write(rendered_template)
print("README.md generated")
