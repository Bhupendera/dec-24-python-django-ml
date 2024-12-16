# Hands-On Project: Decision Tree, Random Forest, and K-Means Clustering with Titanic Dataset

This project demonstrates the implementation of **Decision Tree**, **Random Forest**, and **K-Means Clustering** algorithms using the Titanic dataset.

---

## 1. Introduction to the Dataset

We will use the Titanic dataset, available as a CSV file on [Kaggle](https://www.kaggle.com/c/titanic/data) or a GitHub repository. This dataset contains information about Titanic passengers, including demographic details, ticket class, and survival status.

### Data Columns:
- `PassengerId`: Unique identifier for each passenger.
- `Survived`: Survival status (0 = No, 1 = Yes).
- `Pclass`: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd).
- `Name`: Passenger’s name.
- `Sex`: Gender of the passenger.
- `Age`: Age of the passenger.
- `SibSp`: Number of siblings/spouses aboard.
- `Parch`: Number of parents/children aboard.
- `Ticket`: Ticket number.
- `Fare`: Passenger fare.
- `Cabin`: Cabin number.
- `Embarked`: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

---

## 2. Data Preprocessing

### Step 1: Import Required Libraries
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
```

### Step 2: Load the Dataset
We will load the Titanic dataset from a GitHub repository:

```python
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)
print(data.head())
```

### Step 3: Handle Missing Values
```python
# Fill missing values in 'Age' with the median
data['Age'].fillna(data['Age'].median(), inplace=True)

# Fill missing values in 'Embarked' with the mode
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' due to high percentage of missing values
data.drop('Cabin', axis=1, inplace=True)
```

### Step 4: Encode Categorical Variables
```python
# Encode 'Sex' and 'Embarked'
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
```

### Step 5: Feature Selection
```python
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = data[features]
y = data['Survived']
```

### Step 6: Train-Test Split
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

## 3. Decision Tree Classifier

### Step 1: Train the Model
```python
# Initialize and train the model
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)
```

### Step 2: Evaluate the Model
```python
# Make predictions
y_pred = decision_tree.predict(X_test)

# Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
```
---

## 4. Random Forest Classifier

### Step 1: Train the Model
```python
# Initialize and train the model
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest.fit(X_train, y_train)
```

### Step 2: Evaluate the Model
```python
# Make predictions
y_pred_rf = random_forest.predict(X_test)

# Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
```


---

## 5. K-Means Clustering

### Step 1: Train the Model
For K-Means, we will drop the `Survived` column and cluster passengers based on their features.

```python
# Prepare data for clustering
X_clustering = X.copy()

# Initialize and train the model
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_clustering)

# Add cluster labels to the dataset
data['Cluster'] = kmeans.labels_
```

### Step 2: Visualize Clusters
```python
# Plot clusters
plt.scatter(X_clustering['Age'], X_clustering['Fare'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('K-Means Clustering')
plt.show()
```
