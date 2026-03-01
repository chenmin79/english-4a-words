# Django Backend Skeleton

This folder contains a Django + DRF backend skeleton for the English words project.

## Quick Start

1. Create a virtual environment and install dependencies:
   - `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and update database settings.
3. Run migrations:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
4. Create an admin user:
   - `python manage.py createsuperuser`
5. Start server:
   - `python manage.py runserver`

## Planned Next Steps

- Import 4A/4B vocab JSON using `python manage.py import_vocab ...`
- Connect the existing frontend to `api/study/*` endpoints
- Add Redis/Celery and Channels in later phases

