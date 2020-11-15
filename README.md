# Startup Project (FUN Project)

## Requirements
- Python >= v3.6
- Django >= 3.0

## Setup
1. Install requirements.txt (virtual environment is highly recommended!) `pip install -r requirements.txt`
2. Create .env file `cp .env.example .env`
3. Create settings file `cp config/settings/local.example.py config/settings/local.py`
4. Choose your Database Setup (e.g. Postgres or sqlite3 // sqlite3 is okay for local dev)
5. Check .env file and add required data
6. Migrate Database `python manage.py migrate`
7. Createsuperuser `python manage.py createsuperuser`
8. Runserver `python manage.py runserver`
