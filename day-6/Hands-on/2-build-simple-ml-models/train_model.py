import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle
import os
import traceback


def create_directories():
    try:
        os.makedirs("training-data", exist_ok=True)
        os.makedirs("test-data", exist_ok=True)
        print("Directories created successfully.")
    except Exception as e:
        print("Error creating directories:")
        traceback.print_exc()


def load_data(url):
    try:
        data = pd.read_csv(url)
        print("Dataset loaded successfully.")
        return data
    except Exception as e:
        print("Error loading dataset:")
        traceback.print_exc()
        exit()


def clean_data(data):
    try:
        data = data.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)
        data["Age"] = data["Age"].fillna(data["Age"].median())
        data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])
        data = data.dropna(subset=["Fare"])
        print("Data cleaned successfully.")
        return data
    except Exception as e:
        print("Error during data cleaning:")
        traceback.print_exc()
        exit()


def encode_data(data):
    try:
        data = pd.get_dummies(data, columns=["Sex", "Embarked"], drop_first=True)
        print("Data encoded successfully.")
        return data
    except Exception as e:
        print("Error during data encoding:")
        traceback.print_exc()
        exit()


def split_data(data):
    try:
        X = data.drop("Survived", axis=1)
        y = data["Survived"]
        return train_test_split(X, y, test_size=0.2, random_state=42)
    except Exception as e:
        print("Error during data splitting:")
        traceback.print_exc()
        exit()


def train_model(X_train, y_train):
    try:
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        print("Model trained successfully.")
        return model
    except Exception as e:
        print("Error during model training:")
        traceback.print_exc()
        exit()


def save_model(model, filename="model.pkl"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(model, f)
        print(f"Model saved to {filename}.")
    except Exception as e:
        print("Error saving model:")
        traceback.print_exc()


def save_data(data, filepath):
    try:
        data.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}.")
    except Exception as e:
        print(f"Error saving data to {filepath}:")
        traceback.print_exc()


def evaluate_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

        # Save test data with predictions
        test_data = X_test.copy()
        test_data["Actual"] = y_test
        test_data["Predicted"] = y_pred
        save_data(test_data, "test-data/test_data_with_predictions.csv")
    except Exception as e:
        print("Error during model evaluation:")
        traceback.print_exc()


def main():
    create_directories()
    dataset_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    data = load_data(dataset_url)
    data = clean_data(data)
    data = encode_data(data)

    # Save full training data
    save_data(data, "training-data/full_training_data.csv")

    X_train, X_test, y_train, y_test = split_data(data)
    save_data(pd.concat([X_train, y_train], axis=1), "training-data/training_data.csv")

    model = train_model(X_train, y_train)
    save_model(model)
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()
