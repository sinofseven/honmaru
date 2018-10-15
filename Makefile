SHELL = /usr/bin/env bash -xeuo pipefail

lint:
	@pipenv run flake8 src

test-unit:
	PYTHONPATH=./src \
	pipenv run pytest tests/unit