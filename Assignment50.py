import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report


Border = "-" * 60


# Step 1 : Load the dataset

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Data = load_breast_cancer()

df = pd.DataFrame(Data.data, columns=Data.feature_names)

df["Target"] = Data.target

print("Dataset loaded successfully")
print("First 5 records:")
print(df.head())


# Step 2 : Explore the dataset

print(Border)
print("Step 2 : Explore the dataset")
print(Border)

print("Shape of dataset:")
print(df.shape)

print("Column names:")
print(df.columns)

print("Dataset information:")
print(df.info())

print("Target distribution:")
print(df["Target"].value_counts())


# Step 3 : Check missing values

print(Border)
print("Step 3 : Check missing values")
print(Border)

print("Missing values:")
print(df.isnull().sum())


# Step 4 : Summary statistics

print(Border)
print("Step 4 : Summary statistics")
print(Border)

print(df.describe())


# Step 5 : Exploratory Data Analysis

print(Border)
print("Step 5 : Exploratory Data Analysis")
print(Border)

plt.figure(figsize=(12, 8))

sns.heatmap(
    df.corr(),
    cmap="coolwarm",
    annot=False
)

plt.title("Feature Correlation Heatmap")
plt.show()


# Step 6 : Separate features and target

print(Border)
print("Step 6 : Separate features and target")
print(Border)

X = df.drop("Target", axis=1)

Y = df["Target"]

print("Features shape:", X.shape)
print("Target shape:", Y.shape)


# Step 7 : Split dataset into training and testing sets

print(Border)
print("Step 7 : Split dataset")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)


# Step 8 : Feature Scaling

print(Border)
print("Step 8 : Feature Scaling")
print(Border)

Scaler = StandardScaler()

X_train = Scaler.fit_transform(X_train)

X_test = Scaler.transform(X_test)

print("Feature scaling completed")


# Step 9 : Build the Logistic Regression model

print(Border)
print("Step 9 : Build Logistic Regression model")
print(Border)

Model = LogisticRegression(max_iter=1000)

Model.fit(X_train, Y_train)

print("Model training completed")


# Step 10 : Make predictions

print(Border)
print("Step 10 : Make predictions")
print(Border)

Y_pred = Model.predict(X_test)

print("Predictions:")
print(Y_pred)


# Step 11 : Calculate Accuracy

print(Border)
print("Step 11 : Accuracy")
print(Border)

Accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy:", Accuracy)
print("Accuracy Percentage:", Accuracy * 100, "%")


# Step 12 : Confusion Matrix

print(Border)
print("Step 12 : Confusion Matrix")
print(Border)

CM = confusion_matrix(Y_test, Y_pred)

print(CM)

plt.figure(figsize=(6, 5))

sns.heatmap(
    CM,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Malignant", "Benign"],
    yticklabels=["Malignant", "Benign"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# Step 13 : Precision, Recall and F1-Score

print(Border)
print("Step 13 : Classification Report")
print(Border)

Report = classification_report(
    Y_test,
    Y_pred,
    target_names=["Malignant", "Benign"]
)

print(Report)


# Step 14 : Final conclusion

print(Border)
print("Step 14 : Conclusion")
print(Border)

print("Breast Cancer Prediction completed successfully.")

print("The Logistic Regression model was trained")
print("using the Breast Cancer Wisconsin dataset.")

print("The model predicts whether a tumor is")
print("Malignant or Benign based on medical features.")

print("Accuracy:", Accuracy * 100, "%")