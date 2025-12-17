# Fruits Backend (Django)

This repository contains the backend for the Fruits project.  
It provides fruit data via a simple HTTP API and is intended to be consumed by a separate frontend application.

## Tech Stack

- Python
- Django
- SQLite (default, local development)

## Setup

# Clone the repository

git clone <REPO-URL>
cd fruits_backend

# Create and activate virtual environment

python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

# Start development server

python manage.py runserver

## API

After starting the server, the backend is available at:

http://127.0.0.1:8000/

Example endpoints (depending on current implementation):

- /api/
- /api/fruits/

## Project Structure (simplified)

fruits_backend/
├─ core/
├─ fruits_app/
├─ manage.py
├─ requirements.txt
└─ README.md

## Status

- Development stage: local / work in progress
- Purpose: learning project with focus on clean structure and backend–frontend separation
