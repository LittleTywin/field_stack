#!/bin/sh

set -e

echo "CREATE WAIT_FOR_DB COMMAND"
echo "JUST SLEEPING FOR NOW"
sleep 5

python manage.py migrate
python manage.py runserver 0.0.0.0:8000