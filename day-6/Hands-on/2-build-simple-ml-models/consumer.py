import pandas as pd
import pickle
import random
import traceback


def load_model(filename="model.pkl"):
    try:
        with open(filename, "rb") as f:
            model = pickle.load(f)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print("Error loading model:")
        traceback.print_exc()
        exit()


def generate_random_data():
    try:
        random_data = {
            "Pclass": [random.choice([1, 2, 3])],
            "Age": [round(random.uniform(1, 80), 2)],  # Age between 1 and 80
            "SibSp": [random.randint(0, 5)],  # Number of siblings/spouses
            "Parch": [random.randint(0, 5)],  # Number of parents/children
            "Fare": [round(random.uniform(5, 100), 2)],  # Fare range
            "Sex_male": [random.choice([0, 1])],  # Male or female
            "Embarked_Q": [random.choice([0, 1])],  # Embarked Q
            "Embarked_S": [random.choice([0, 1])],  # Embarked S
        }
        print("Random data generated successfully.")
        return pd.DataFrame(random_data)
    except Exception as e:
        print("Error generating random data:")
        traceback.print_exc()
        exit()


def predict(model, data):
    try:
        prediction = model.predict(data)[0]
        print("\nGenerated Data:")
        print(data)
        print(f"Predicted Survival: {'Survived' if prediction == 1 else 'Did Not Survive'}")
    except Exception as e:
        print("Error during prediction:")
        traceback.print_exc()


def main():
    model = load_model()
    for _ in range(3):  # Make 3 predictions
        random_data = generate_random_data()
        predict(model, random_data)


if __name__ == "__main__":
    main()
