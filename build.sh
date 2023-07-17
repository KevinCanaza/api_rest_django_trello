#!/bin/bash

# Build the project

echo "Building the project..."

python - m pip install - r requeriments.txt

echo "Make Migration..."
python manage.py makemigrations --noinput
python manaye.py migrate -noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear


