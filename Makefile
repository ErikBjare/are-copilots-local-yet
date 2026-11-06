# README.md is a pure function of the committed data (offline, deterministic).
README.md: README.md.in data/data.yaml data/metadata.yaml scripts/generate_readme.py scripts/status.py
	python3 scripts/generate_readme.py

# Network: refresh stars/activity (set GITHUB_TOKEN to avoid rate limits).
.PHONY: refresh check
refresh:
	python3 scripts/refresh.py

check:
	python3 scripts/validate.py
	python3 -m pytest -q tests
