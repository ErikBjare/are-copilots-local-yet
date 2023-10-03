README.md: README.md.in data/metadata.yaml
	python3 scripts/generate_readme.py

.PHONY: data/metadata.yaml
data/metadata.yaml:
	python3 scripts/update_metadata.py
