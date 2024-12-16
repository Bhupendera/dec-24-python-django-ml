import requests
import random

# Flask API URL
url = "http://127.0.0.1:5000/predict"

# Function to generate random Titanic passenger data
def generate_random_passenger_data():
    return {
        "Pclass": random.choice([1, 2, 3]),  # Random class (1st, 2nd, 3rd)
        "Age": round(random.uniform(1, 80), 2),  # Random age between 1 and 80
        "SibSp": random.randint(0, 5),  # Random number of siblings/spouses
        "Parch": random.randint(0, 5),  # Random number of parents/children
        "Fare": round(random.uniform(5, 100), 2),  # Random fare
        "Sex_male": random.choice([0, 1]),  # Randomly Male (1) or Female (0)
        "Embarked_Q": random.choice([0, 1]),  # Randomly embarked at Q
        "Embarked_S": random.choice([0, 1]),  # Randomly embarked at S
    }

# Function to call the Flask API
def make_prediction():
    # Generate random passenger data
    passenger_data = generate_random_passenger_data()
    
    try:
        # Send POST request to the Flask API
        response = requests.post(url, json=passenger_data)
        response.raise_for_status()  # Raise exception for HTTP errors
        prediction = response.json().get("prediction", "No prediction returned")

        # Print the input data and prediction
        print("\nPassenger Data:")
        for key, value in passenger_data.items():
            print(f"  {key}: {value}")
        print(f"\nPrediction: {prediction}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Main function to repeatedly make predictions
if __name__ == "__main__":
    print("Testing Flask API with random passenger data...\n")
    for _ in range(3):  # Generate and test 3 random passengers
        make_prediction()
