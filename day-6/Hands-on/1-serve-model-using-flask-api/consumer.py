import requests
import pandas as pd
import argparse

# Define the mapping from numeric predictions to class names
class_mapping = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica",
    3: "Unknown"  # Add this if your model can predict 3
}

def get_prediction(json_data):
    url = "http://127.0.0.1:5000/predict"  # Flask API URL
    response = requests.post(url, json={"features": json_data})
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        # Map the numeric prediction to the class name
        return class_mapping.get(prediction, "Unknown")
    else:
        return response.json().get("error", "Error occurred")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get prediction for a specific record from CSV")
    parser.add_argument("record_no", type=int, help="Record number to get prediction for")
    args = parser.parse_args()

    csv_file_path = "c-features.csv"  # Replace with the correct path to your CSV
    data = pd.read_csv(csv_file_path)
    
    if args.record_no < 0 or args.record_no >= len(data):
        print("Invalid record number")
    else:
        record = data.iloc[[args.record_no]]
        json_data = record.to_dict(orient="records")[0]  # Single dictionary
        print(json_data)

        prediction = get_prediction(json_data)

        print(prediction)