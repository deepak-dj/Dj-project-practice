#!/bin/bash
sleep 1
python manage.py migrate

exec python manage.py runserver
