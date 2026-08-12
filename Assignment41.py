import pandas as pd
import numpy as np

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


Border = "-" * 60


# ============================================================
# STEP 1 : GET DATA
# ============================================================

print(Border)
print("STEP 1 : GET DATA")
print(Border)

Wine = load_wine()

df = pd.DataFrame(
    Wine.data,
    columns=Wine.feature_names
)

df["Class"] = Wine.target

print("First 5 Records:")
print(df.head())

print("Dataset Shape:")
print(df.shape)

print("Column Names:")
print(df.columns)


# ============================================================
# STEP 2 : CLEAN, PREPARE & MANIPULATE DATA
# ============================================================

print(Border)
print("STEP 2 : CLEAN, PREPARE & MANIPULATE DATA")
print(Border)

print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Records:")
print(df.duplicated().sum())

X = df.drop("Class", axis=1)

Y = df["Class"]

print("Features:")
print(X.head())

print("Target:")
print(Y.head())


# ============================================================
# STEP 3 : TRAIN DATA
# ============================================================

print(Border)
print("STEP 3 : TRAIN DATA")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42,
    stratify=Y
)

print("Training Data Shape:")
print(X_train.shape)

print("Testing Data Shape:")
print(X_test.shape)

Scaler = StandardScaler()

X_train = Scaler.fit_transform(X_train)

X_test = Scaler.transform(X_test)

Model = DecisionTreeClassifier(
    random_state=42
)

Model.fit(X_train, Y_train)

print("Model Training Completed Successfully.")


# ============================================================
# STEP 4 : TEST DATA
# ============================================================

print(Border)
print("STEP 4 : TEST DATA")
print(Border)

Y_Pred = Model.predict(X_test)

print("Actual Values:")
print(Y_test.values)

print("Predicted Values:")
print(Y_Pred)


# ============================================================
# STEP 5 : CALCULATE ACCURACY
# ============================================================

print(Border)
print("STEP 5 : CALCULATE ACCURACY")
print(Border)

Accuracy = accuracy_score(Y_test, Y_Pred)

print("Model Accuracy:")
print(Accuracy)

print("Accuracy Percentage:")
print(Accuracy * 100, "%")


print(Border)
print("CONFUSION MATRIX")
print(Border)

CM = confusion_matrix(Y_test, Y_Pred)

print(CM)


print(Border)
print("CLASSIFICATION REPORT")
print(Border)

print(
    classification_report(
        Y_test,
        Y_Pred,
        target_names=Wine.target_names
    )
)


print(Border)
print("FINAL RESULT")
print(Border)

print("Wine Classification Completed Successfully.")

print("Final Accuracy =", Accuracy * 100, "%")