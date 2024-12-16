import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

class FlowerClassifier:
    def __init__(self, model, target_names):
        self.model = model
        self.target_names = target_names

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def predict_flower_names(self, X):
        predictions = self.predict(X)
        return [self.target_names[label] for label in predictions]

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target labels
target_names = iris.target_names  # Flower names

# Convert target labels to flower names
y_flower_names = [target_names[label] for label in y]

# Convert to DataFrame for saving as CSV
X_df = pd.DataFrame(X, columns=iris.feature_names)
y_df = pd.DataFrame(y_flower_names, columns=["target"])

# Save to CSV files
X_df.to_csv("training-data/X.csv", index=False)
y_df.to_csv("training-data/y.csv", index=False)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
base_model = RandomForestClassifier(random_state=42)
model = FlowerClassifier(base_model, target_names)
model.fit(X_train, y_train)

# Test the model and print the accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Convert predicted labels to flower names
y_pred_flower_names = model.predict_flower_names(X_test)

# Save the trained model to a file
model_file = "model.pkl"
with open(model_file, "wb") as f:
    pickle.dump(model, f)

print(f"Trained model saved as '{model_file}'")

# Print predicted flower names
print("Predicted flower names:", y_pred_flower_names)

# Combine test features, real labels, and predicted labels into a DataFrame
test_data = pd.DataFrame(X_test, columns=iris.feature_names)
test_data["real_label"] = [target_names[label] for label in y_test]
test_data["predicted_label"] = y_pred_flower_names

# Save the combined DataFrame to a CSV file
test_data.to_csv("test-data/test_results.csv", index=False)

print("Test results saved as 'test-data/test_results.csv'")