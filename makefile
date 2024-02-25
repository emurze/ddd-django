
# Variables

DOCKER_CONTAINER_NAME = drf.api


# Functions

define docker_exec
	docker exec -it ${DOCKER_CONTAINER_NAME} bash -c "$(1)"
endef

define docker_row_exec
	docker exec ${DOCKER_CONTAINER_NAME} bash -c "$(1)"
endef


# Run

run:
	docker compose up --build


# Migrations

migrations:
	$(call docker_exec,cd src && poetry run python manage.py makemigrations)

migrate:
	$(call docker_exec,cd src && poetry run python manage.py migrate)


# Shell

shell:
	$(call docker_exec,cd src && poetry run python manage.py shell)


# Tests

black:
	poetry run black . -l 79 tests src

lint:
	poetry run flake8 --config setup.cfg src tests

typechecks:
	cd src && poetry run mypy --config ../setup.cfg .

integration_tests:
	$(call docker_exec,poetry run pytest -s -vv src/apps/)

test: lint typechecks integration_tests
