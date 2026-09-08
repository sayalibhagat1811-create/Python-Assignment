import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Load the Employee Attrition dataset
df = pd.read_csv('Employee_Attrition.csv')

print("Shape of Dataset:", df.shape)

print("Columns:")
print(df.columns)

print("First Five Records:")
print(df.head())

# Check whether the dataset contains missing values
print("Missing Values:")
print(df.isnull().sum())

# Identify numerical and categorical columns
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
categorical_features = df.select_dtypes(include=['object']).columns

print("Numerical Features:")
print(numerical_features)

print("Categorical Features:")
print(categorical_features)

# Convert OverTime from Yes/No into 1/0
df['OverTime'] = df['OverTime'].map({
    'Yes': 1,
    'No': 0
})

# Convert target Attrition from Yes/No into 1/0
df['Attrition'] = df['Attrition'].map({
    'Yes': 1,
    'No': 0
})

# X contains input features and y contains the target
X = df.drop('Attrition', axis=1)
y = df['Attrition']

# Split data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Scale features so that all values are on a similar scale
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create MLP neural network with two hidden layers
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

# Train the neural network
model.fit(X_train_scaled, y_train)

print("Model Training Completed")

# Display number of iterations used by the model
print("Number of Iterations:", model.n_iter_)

# Predict results for training and testing data
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

# Calculate training and testing accuracy
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("Training Accuracy:", train_accuracy * 100, "%")
print("Testing Accuracy:", test_accuracy * 100, "%")

# Display precision, recall and F1-score
print("Classification Report:")
print(classification_report(
    y_test,
    y_test_pred,
    zero_division=0
))

# Create confusion matrix
cm = confusion_matrix(y_test, y_test_pred)

print("Confusion Matrix:")
print(cm)

# Display confusion matrix graphically
plt.figure(figsize=(6, 5))

plt.imshow(cm)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.xticks([0, 1], ['Stay', 'Leave'])
plt.yticks([0, 1], ['Stay', 'Leave'])

# Display values inside the confusion matrix
for i in range(2):
    for j in range(2):
        plt.text(
            j,
            i,
            cm[i, j],
            ha='center',
            va='center'
        )

plt.colorbar()
plt.show()

# Plot the loss curve to see how the model learned
plt.figure(figsize=(8, 5))

plt.plot(model.loss_curve_)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.grid()
plt.show()

# Function to predict whether a new employee will leave or stay
def PredictAttrition(employee_data):

    # Convert new employee data into a DataFrame
    employee_df = pd.DataFrame(
        [employee_data],
        columns=X.columns
    )

    # Apply the same scaling used during model training
    employee_scaled = scaler.transform(employee_df)

    # Predict employee attrition
    prediction = model.predict(employee_scaled)

    # Get probability of Stay and Leave
    probability = model.predict_proba(employee_scaled)

    if prediction[0] == 1:
        result = "Employee is likely to LEAVE"
    else:
        result = "Employee is likely to STAY"

    print("Prediction:", result)
    print("Probability of Staying:", probability[0][0])
    print("Probability of Leaving:", probability[0][1])

    return prediction[0]

# New employee record 1
employee1 = [
    25, 2500, 1, 3, 20,
    2, 2, 1, 4, 2
]

# New employee record 2
employee2 = [
    45, 8000, 12, 20, 5,
    4, 4, 0, 1, 4
]

# New employee record 3
employee3 = [
    29, 3000, 2, 5, 15,
    2, 2, 1, 3, 1
]

# New employee record 4
employee4 = [
    38, 6500, 8, 12, 3,
    4, 3, 0, 2, 3
]

# New employee record 5
employee5 = [
    52, 9000, 15, 25, 2,
    4, 4, 0, 1, 4
]

# Test the model on five new employees
print("Employee 1")
PredictAttrition(employee1)

print("Employee 2")
PredictAttrition(employee2)

print("Employee 3")
PredictAttrition(employee3)

print("Employee 4")
PredictAttrition(employee4)

print("Employee 5")
PredictAttrition(employee5)

# Compare training and testing accuracy to identify overfitting
difference = train_accuracy - test_accuracy

print("Training Accuracy:", train_accuracy * 100, "%")
print("Testing Accuracy:", test_accuracy * 100, "%")

if difference > 0.10:
    print("Model may be suffering from OVERFITTING")
elif train_accuracy < 0.70 and test_accuracy < 0.70:
    print("Model may be suffering from UNDERFITTING")
else:
    print("Model appears to have reasonable generalization")