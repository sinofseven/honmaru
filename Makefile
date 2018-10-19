SHELL = /usr/bin/env bash -xeuo pipefail

lint:
	@pipenv run flake8 src/ tests/

test-unit:
	OLD_DIR=$$PWD; \
	cd tests/unit; \
	PYTHONPATH=../../src \
	pipenv run pytest . ; \
	cd $$OLD_DIR