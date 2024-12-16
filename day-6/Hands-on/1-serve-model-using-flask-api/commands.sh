python -m venv myvenv
myvenv\Scripts\activate

pip install -r requirements.txt

python train_model.py

python app.py


python consumer.py 1
python consumer.py 2
python consumer.py 3



