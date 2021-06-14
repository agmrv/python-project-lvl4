install:
	@poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run coverage run --source 'task_manager' manage.py test

selfcheck:
	poetry check

check: selfcheck lint test
	python manage.py check

build: check
	poetry build

package-install: build
	pip install --user dist/*.whl

requirements:
	poetry export -f requirements.txt --without-hashes --output requirements.txt

runserver:
	python manage.py runserver

deploy: check requirements
	git push heroku main
	heroku ps

messages:
	django-admin makemessages -a -l ru

compilemessages:
	django-admin compilemessages

migrate:
	python manage.py makemigrations
	python manage.py migrate

heroku-migrate:
	heroku run python manage.py migrate

.PHONY: install lint test selfcheck check build publish requirements runserver deploy messages compilemessages migrate heroku-migrate
