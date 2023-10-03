README.md: README.md.in metadata.yaml
	python3 generate_readme.py

.PHONY: metadata.yaml
metadata.yaml:
	python3 update_metadata.py
