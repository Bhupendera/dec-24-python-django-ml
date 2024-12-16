python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

python flask_api.py

## Start new terminal and run:
venv\Scripts\activate
python test_api.py

## Setup django project
django-admin startproject TitanicPredictor
cd TitanicPredictor
python manage.py startapp passengers
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations passengers
python manage.py migrate
python manage.py runserver
