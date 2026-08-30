import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix


Border = "-" * 60


# Step 1 : Load the dataset

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "Fraudulent_Transaction_Detection.csv"

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

X = df.drop("Fraud", axis=1)
Y = df["Fraud"]

print("Input variables :")
print(X.head())

print("Output variable :")
print(Y.head())


# Step 4 : Convert categorical data into numerical data

print(Border)
print("Step 4 : Convert categorical data into numerical data")
print(Border)

X = pd.get_dummies(X, drop_first=True)

print("Data converted successfully")
print(X.head())


# Step 5 : Split the dataset

print(Border)
print("Step 5 : Split the dataset")
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


# Step 6 : Train Decision Tree

print(Border)
print("Step 6 : Train Decision Tree")
print(Border)

DecisionTreeModel = DecisionTreeClassifier(
    random_state=42
)

DecisionTreeModel.fit(X_train, Y_train)

DecisionTreePrediction = DecisionTreeModel.predict(X_test)


# Step 7 : Train Bagging Classifier

print(Border)
print("Step 7 : Train Bagging Classifier")
print(Border)

BaggingModel = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=10,
    random_state=42
)

BaggingModel.fit(X_train, Y_train)

BaggingPrediction = BaggingModel.predict(X_test)


# Step 8 : Train Random Forest Classifier

print(Border)
print("Step 8 : Train Random Forest Classifier")
print(Border)

RandomForestModel = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

RandomForestModel.fit(X_train, Y_train)

RandomForestPrediction = RandomForestModel.predict(X_test)


# Step 9 : Train AdaBoost Classifier

print(Border)
print("Step 9 : Train AdaBoost Classifier")
print(Border)

AdaBoostModel = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

AdaBoostModel.fit(X_train, Y_train)

AdaBoostPrediction = AdaBoostModel.predict(X_test)


# Step 10 : Create Voting Classifier

print(Border)
print("Step 10 : Create Voting Classifier")
print(Border)

VotingModel = VotingClassifier(
    estimators=[
        ("DecisionTree", DecisionTreeClassifier(random_state=42)),
        ("RandomForest", RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )),
        ("AdaBoost", AdaBoostClassifier(
            n_estimators=50,
            random_state=42
        ))
    ],
    voting="hard"
)

VotingModel.fit(X_train, Y_train)

VotingPrediction = VotingModel.predict(X_test)


# Step 11 : Calculate Decision Tree metrics

print(Border)
print("Step 11 : Decision Tree Evaluation")
print(Border)

DTAccuracy = accuracy_score(Y_test, DecisionTreePrediction)
DTPrecision = precision_score(Y_test, DecisionTreePrediction, zero_division=0)
DTRecall = recall_score(Y_test, DecisionTreePrediction, zero_division=0)
DTF1 = f1_score(Y_test, DecisionTreePrediction, zero_division=0)
DTConfusionMatrix = confusion_matrix(Y_test, DecisionTreePrediction)

print("Accuracy :", DTAccuracy)
print("Precision :", DTPrecision)
print("Recall    :", DTRecall)
print("F1 Score  :", DTF1)
print("Confusion Matrix :")
print(DTConfusionMatrix)


# Step 12 : Calculate Bagging metrics

print(Border)
print("Step 12 : Bagging Evaluation")
print(Border)

BagAccuracy = accuracy_score(Y_test, BaggingPrediction)
BagPrecision = precision_score(Y_test, BaggingPrediction, zero_division=0)
BagRecall = recall_score(Y_test, BaggingPrediction, zero_division=0)
BagF1 = f1_score(Y_test, BaggingPrediction, zero_division=0)
BagConfusionMatrix = confusion_matrix(Y_test, BaggingPrediction)

print("Accuracy :", BagAccuracy)
print("Precision :", BagPrecision)
print("Recall    :", BagRecall)
print("F1 Score  :", BagF1)
print("Confusion Matrix :")
print(BagConfusionMatrix)


# Step 13 : Calculate Random Forest metrics

print(Border)
print("Step 13 : Random Forest Evaluation")
print(Border)

RFAccuracy = accuracy_score(Y_test, RandomForestPrediction)
RFPrecision = precision_score(Y_test, RandomForestPrediction, zero_division=0)
RFRecall = recall_score(Y_test, RandomForestPrediction, zero_division=0)
RFF1 = f1_score(Y_test, RandomForestPrediction, zero_division=0)
RFConfusionMatrix = confusion_matrix(Y_test, RandomForestPrediction)

print("Accuracy :", RFAccuracy)
print("Precision :", RFPrecision)
print("Recall    :", RFRecall)
print("F1 Score  :", RFF1)
print("Confusion Matrix :")
print(RFConfusionMatrix)


# Step 14 : Calculate AdaBoost metrics

print(Border)
print("Step 14 : AdaBoost Evaluation")
print(Border)

ABAccuracy = accuracy_score(Y_test, AdaBoostPrediction)
ABPrecision = precision_score(Y_test, AdaBoostPrediction, zero_division=0)
ABRecall = recall_score(Y_test, AdaBoostPrediction, zero_division=0)
ABF1 = f1_score(Y_test, AdaBoostPrediction, zero_division=0)
ABConfusionMatrix = confusion_matrix(Y_test, AdaBoostPrediction)

print("Accuracy :", ABAccuracy)
print("Precision :", ABPrecision)
print("Recall    :", ABRecall)
print("F1 Score  :", ABF1)
print("Confusion Matrix :")
print(ABConfusionMatrix)


# Step 15 : Calculate Voting metrics

print(Border)
print("Step 15 : Voting Classifier Evaluation")
print(Border)

VotingAccuracy = accuracy_score(Y_test, VotingPrediction)
VotingPrecision = precision_score(Y_test, VotingPrediction, zero_division=0)
VotingRecall = recall_score(Y_test, VotingPrediction, zero_division=0)
VotingF1 = f1_score(Y_test, VotingPrediction, zero_division=0)
VotingConfusionMatrix = confusion_matrix(Y_test, VotingPrediction)

print("Accuracy :", VotingAccuracy)
print("Precision :", VotingPrecision)
print("Recall    :", VotingRecall)
print("F1 Score  :", VotingF1)
print("Confusion Matrix :")
print(VotingConfusionMatrix)


# Step 16 : Final Comparison

print(Border)
print("Step 16 : Final Model Comparison")
print(Border)

Comparison = pd.DataFrame({
    "Algorithm": [
        "Decision Tree",
        "Bagging",
        "Random Forest",
        "AdaBoost",
        "Voting"
    ],
    "Accuracy": [
        DTAccuracy,
        BagAccuracy,
        RFAccuracy,
        ABAccuracy,
        VotingAccuracy
    ],
    "Precision": [
        DTPrecision,
        BagPrecision,
        RFPrecision,
        ABPrecision,
        VotingPrecision
    ],
    "Recall": [
        DTRecall,
        BagRecall,
        RFRecall,
        ABRecall,
        VotingRecall
    ],
    "F1 Score": [
        DTF1,
        BagF1,
        RFF1,
        ABF1,
        VotingF1
    ]
})

print(Comparison)