#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

cd "$SCRIPT_DIR"

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd car_api
python3 manage.py test
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
#echo "Current directory: $(pwd)"
