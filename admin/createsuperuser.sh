#!/bin/bash

docker-compose run --rm djangoapp sh -c "python manage.py createsuperuser"