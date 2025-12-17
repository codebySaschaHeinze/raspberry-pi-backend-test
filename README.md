# Fruits Backend (Django on Raspberry Pi)

A small learning backend built with Django and hosted on a Raspberry Pi.  
It serves a JSON API that is consumed by a separate frontend running on a laptop in the same local network.

## Goal
Practice a real client–server setup:
- Backend runs on the Raspberry Pi
- Frontend runs on the laptop
- Communication happens via HTTP + JSON (and CORS)

## Tech Stack
- Python
- Django
- SQLite (default Django DB)
- django-cors-headers (CORS for separate frontend)

## Project Layout
fruits-backend/
- core/            Django project (settings, urls, asgi/wsgi)
- fruits_app/      Django app providing the /fruits/ endpoint
- manage.py
- requirements.txt
- .gitignore
- .venv/           Virtual environment (not committed)

## Setup (Raspberry Pi)
cd ~/projects/fruits-backend

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate

## Run (LAN-accessible)
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8000

## API
GET /fruits/

Example:
http://192.168.0.96:8000/fruits/

## Required Django Settings
### ALLOWED_HOSTS
To access the backend from your laptop, add the Pi IP (without port) to ALLOWED_HOSTS in core/settings.py:

ALLOWED_HOSTS = [
  "127.0.0.1",
  "localhost",
  "192.168.0.96",
]

### CORS (Frontend on Laptop)
If the frontend runs via VS Code Live Server (commonly port 5500), allow those origins in core/settings.py:

CORS_ALLOWED_ORIGINS = [
  "http://127.0.0.1:5500",
  "http://localhost:5500",
]

## Common Problems
- DisallowedHost: Pi IP missing in ALLOWED_HOSTS
- CORS error in browser console: frontend origin missing in CORS_ALLOWED_ORIGINS
- ERR_CONNECTION_REFUSED: server not running or wrong IP

## Notes
- 0.0.0.0 is a server bind address, not a browser URL
- This is a learning project (kept intentionally simple)

License: Private learning project.
