#!/bin/bash

docker-compose run --rm django_app sh -c "python manage.py makemigrations"