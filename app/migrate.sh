#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}

cd /app/

/opt/venv/bin/python3 manage.py migrate --noinput || true

/opt/venv/bin/python3 manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
