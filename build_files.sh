#!/bin/bash

#build project 
echo "Building Priject..."
pip install -r requirements.txt

# echo "Make Migrations" 

# python manage.py makemigrations --noinput
# python manage.py migrate --noinput

# echo "collect static"
# python manage.py collectstatic --noinput --clear