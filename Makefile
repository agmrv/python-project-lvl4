install:
	@poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run pytest -s -v --verbose --cov=page_loader tests/

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	poetry build

package-install: build
	pip install --user dist/*.whl

requirements:
	poetry export -f requirements.txt --without-hashes --output requirements.txt

.PHONY: install lint test selfcheck check build publish
