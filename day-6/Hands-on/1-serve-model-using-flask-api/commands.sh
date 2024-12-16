python -m venv venv
venv/Scripts/activate

pip install -r requirements.txt

python train-model.py

python app.py


python consumer.py 1
python consumer.py 2
python consumer.py 3



