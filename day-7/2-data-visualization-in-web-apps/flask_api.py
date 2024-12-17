from flask import Flask, request, jsonify
import pickle
import numpy as np
import logging
import traceback
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

# Load the pre-trained model
model_path = "models/model.pkl"
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    logging.error(traceback.format_exc())

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        logging.debug(f"Received data: {data}")
        print(f"Received data: {data}")

        # Prepare input features
        features = np.array([
            data["Pclass"],
            data["Age"],
            data["SibSp"],
            data["Parch"],
            data["Fare"],
            data["Sex_male"],
            data["Embarked_Q"],
            data["Embarked_S"]
        ]).reshape(1, -1)
        logging.debug(f"Prepared features: {features}")

        # Make prediction
        prediction = model.predict(features)[0]
        print("prediction: ", prediction)
        result = "Survived" if prediction == 1 else "Did Not Survive"
        print("result: ", result)
        logging.info(f"Prediction result: {result}")

        return jsonify({"prediction": result})
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        logging.error(traceback.format_exc())
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
