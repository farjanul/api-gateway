#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput --clear
python manage.py create_default_admin

gunicorn -b :8000 --access-logfile - --error-logfile - conf.wsgi #--workers=4