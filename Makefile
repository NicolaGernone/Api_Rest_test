build:
	docker compose build

down:
	docker compose down

up: build makemigrations migrate
	docker compose up -d

first: build makemigrations migrate loaddatacsv
	docker compose up -d

migrate:
	docker compose run --rm api python manage.py migrate

makemigrations:
	docker compose run --rm api python manage.py makemigrations

showmig: 
	docker compose run --rm api python manage.py showmigrations

loaddata:
	docker compose run --rm api python manage.py loaddata data.json

loaddatacsv:
	docker compose run --rm api python manage.py loaddatacsv "./archive"

deps: deps_lock
	docker compose run --rm api poetry install

deps_lock:
	docker compose run --rm api poetry lock

user:
	docker compose run --rm api python manage.py createsuperuser

static:
	docker compose run --rm api python manage.py collectstatic --noinput --clear --no-post-process

bash:
	docker compose run --rm api /bin/sh

test: build makemigrations migrate
	docker compose run --rm api python manage.py test
