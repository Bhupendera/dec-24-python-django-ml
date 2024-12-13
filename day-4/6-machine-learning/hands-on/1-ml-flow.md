## Pre-requisites

```
!pip install numpy
!pip install pandas
!pip install matplotlib
!pip install scikit-learn
```

### Step 1: Data Preparation

Load the dataset into a Pandas DataFrame:
   ```python
   import pandas as pd

   # Load dataset
   url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
   column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
   df = pd.read_csv(url, header=None, names=column_names)

   # Display first few rows
   print(df.head())
   ```

### Step 2: Splitting the Dataset

Split the dataset into training and testing sets:
```python
from sklearn.model_selection import train_test_split

# Split features and target
X = df.drop("species", axis=1)
y = df["species"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

### Step 3: Building and Training a Model

Train the model:
   ```python
   from sklearn.tree import DecisionTreeClassifier

   # Initialize model
   model = DecisionTreeClassifier()

   # Train model
   model.fit(X_train, y_train)
   ```

---

### Step 4: Predict
```
import pandas as pd

# Example data point as a DataFrame
input_data = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])

# Predict class
prediction = model.predict(input_data)
print("Predicted class:", prediction)
```