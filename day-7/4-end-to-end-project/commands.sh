python -m venv myvenv
myvenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

python flask_api.py

## Start new terminal and run:
myvenv\Scripts\activate
python test_api.py

## Setup django project
myvenv\Scripts\activate
cd TitanicPredictor
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations passengers
python manage.py migrate
python manage.py runserver
