python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train the model
python train_model.py

# Run the consumer
python consumer.py
