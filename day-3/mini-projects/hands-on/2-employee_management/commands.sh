python -V
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations employees
python manage.py migrate
python manage.py runserver
