from flask import Flask, request, jsonify
import pickle
import numpy as np
from train_model import FlowerClassifier  # Import the FlowerClassifier class
import traceback

# Initialize Flask app
app = Flask(__name__)

# Load the trained scikit-learn model
MODEL_PATH = "model.pkl"  # Replace with your actual model file path

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# ...existing code...
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON data
        input_data = request.get_json()
        print("input_data: ", input_data)
        if not input_data:
            return jsonify({"error": "No input data provided"}), 400
        
        # Extract feature values
        features = np.array([list(input_data["features"].values())])  # Convert dict to 2D array
        # Perform prediction
        prediction = model.predict(features)[0]  # Assuming single output
        prediction = int(prediction)
        # Return the prediction as JSON
        return jsonify({"prediction": prediction}), 200

    except KeyError:
        traceback.print_stack()
        return jsonify({"error": "Invalid input format. 'features' key is required."}), 400
        
    except Exception as e:
        traceback.print_stack()
        return jsonify({"error": f"An error occurred: {e}"}), 500
        


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
