### Краткое описание проекта

Проект api сервиса для оценки произведений, упакованный в контейнеры с базой данных postgres и сервером nginx, с настройкой workflow для GitHub Actions

### Инструкция по установке Docker

https://docs.docker.com/engine/install/

### Команда для клонирования

git clone https://github.com/alx-git/yamdb_final.git

### Шаблон наполнения env-файла

DB_ENGINE=django.db.backends.postgresql

DB_NAME=postgres 

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

DB_HOST=db 

DB_PORT=5432

ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = test

### Описание команд для работы с контейнерами

docker-compose up -d --build - пересборка и запуск контейнера в фоновом режиме

docker-compose exec web python manage.py migrate - миграции

docker-compose exec web python manage.py createsuperuser - создание суперпользователя

docker-compose exec web python manage.py collectstatic --no-input - сбор статики

docker-compose exec web python manage.py dumpdata > fixtures.json - создание резервной базы данных

docker-compose down -v - остановка и удаление контейнеров

### Технологии

asgiref==3.2.10

Django==2.2.16

django-filter==2.4.0

djangorestframework==3.12.4

djangorestframework-simplejwt==4.8.0

gunicorn==20.0.4

psycopg2-binary==2.8.6

PyJWT==2.1.0

pytz==2020.1

pytest-django

pytest-pythonpath

sqlparse==0.3.1

### Автор

alexander

### Ссылка на проект

http://alexyatube.ddns.net/admin

![example workflow](https://github.com/alx-git/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

--

