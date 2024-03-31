
install:
	poetry install

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run python manage.py migrate
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi


migrations:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate