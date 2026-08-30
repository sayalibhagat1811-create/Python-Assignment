import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


Border = "-" * 60


# Step 1 : Load the dataset

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "Customer_Loan_Approval.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")
print(df.head())


# Step 2 : Check for missing values

print(Border)
print("Step 2 : Check for missing values")
print(Border)

print(df.isnull().sum())


# Step 3 : Separate input and output variables

print(Border)
print("Step 3 : Separate input and output variables")
print(Border)

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]

print("Input variables :")
print(X.head())

print("Output variable :")
print(Y.head())


# Step 4 : Split the dataset into training and testing data

print(Border)
print("Step 4 : Split the dataset")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("Training data :", X_train.shape)
print("Testing data  :", X_test.shape)


# Step 5 : Train Logistic Regression

print(Border)
print("Step 5 : Train Logistic Regression")
print(Border)

LogisticModel = Pipeline([
    ("Scaler", StandardScaler()),
    ("Model", LogisticRegression())
])

LogisticModel.fit(X_train, Y_train)

LogisticPrediction = LogisticModel.predict(X_test)

LogisticAccuracy = accuracy_score(
    Y_test,
    LogisticPrediction
)

print("Logistic Regression Accuracy :", LogisticAccuracy)


# Step 6 : Train Decision Tree

print(Border)
print("Step 6 : Train Decision Tree")
print(Border)

DecisionTreeModel = DecisionTreeClassifier(
    random_state=42
)

DecisionTreeModel.fit(X_train, Y_train)

DecisionTreePrediction = DecisionTreeModel.predict(X_test)

DecisionTreeAccuracy = accuracy_score(
    Y_test,
    DecisionTreePrediction
)

print("Decision Tree Accuracy :", DecisionTreeAccuracy)


# Step 7 : Train KNN

print(Border)
print("Step 7 : Train KNN")
print(Border)

KNNModel = Pipeline([
    ("Scaler", StandardScaler()),
    ("Model", KNeighborsClassifier(n_neighbors=5))
])

KNNModel.fit(X_train, Y_train)

KNNPrediction = KNNModel.predict(X_test)

KNNAccuracy = accuracy_score(
    Y_test,
    KNNPrediction
)

print("KNN Accuracy :", KNNAccuracy)


# Step 8 : Calculate individual accuracy

print(Border)
print("Step 8 : Individual Model Accuracy")
print(Border)

print("Logistic Regression :", LogisticAccuracy)
print("Decision Tree       :", DecisionTreeAccuracy)
print("KNN                 :", KNNAccuracy)


# Step 9 : Create Hard Voting Classifier

print(Border)
print("Step 9 : Create Hard Voting Classifier")
print(Border)

HardVotingModel = VotingClassifier(
    estimators=[
        ("Logistic", LogisticModel),
        ("DecisionTree", DecisionTreeModel),
        ("KNN", KNNModel)
    ],
    voting="hard"
)

HardVotingModel.fit(X_train, Y_train)

HardVotingPrediction = HardVotingModel.predict(X_test)

HardVotingAccuracy = accuracy_score(
    Y_test,
    HardVotingPrediction
)

print("Hard Voting Accuracy :", HardVotingAccuracy)


# Step 10 : Calculate Hard Voting accuracy

print(Border)
print("Step 10 : Hard Voting Accuracy")
print(Border)

print("Hard Voting Classifier Accuracy :", HardVotingAccuracy)


# Step 11 : Create Soft Voting Classifier

print(Border)
print("Step 11 : Create Soft Voting Classifier")
print(Border)

SoftVotingModel = VotingClassifier(
    estimators=[
        ("Logistic", LogisticModel),
        ("DecisionTree", DecisionTreeModel),
        ("KNN", KNNModel)
    ],
    voting="soft"
)

SoftVotingModel.fit(X_train, Y_train)

SoftVotingPrediction = SoftVotingModel.predict(X_test)

SoftVotingAccuracy = accuracy_score(
    Y_test,
    SoftVotingPrediction
)

print("Soft Voting Accuracy :", SoftVotingAccuracy)


# Step 12 : Calculate Soft Voting accuracy

print(Border)
print("Step 12 : Soft Voting Accuracy")
print(Border)

print("Soft Voting Classifier Accuracy :", SoftVotingAccuracy)


# Step 13 : Compare all models

print(Border)
print("Step 13 : Model Comparison")
print(Border)

Comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],
    "Accuracy": [
        LogisticAccuracy,
        DecisionTreeAccuracy,
        KNNAccuracy,
        HardVotingAccuracy,
        SoftVotingAccuracy
    ]
})

print(Comparison)