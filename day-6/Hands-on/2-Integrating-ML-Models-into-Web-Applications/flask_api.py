from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model_path = "models/model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
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
        # Make prediction
        prediction = model.predict(features)[0]
        result = "Survived" if prediction == 1 else "Did Not Survive"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
