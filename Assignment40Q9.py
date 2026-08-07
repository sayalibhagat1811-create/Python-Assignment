import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X = df[["StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours",
        "PerformanceIndex"]]

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(Y_test, prediction)

print("Accuracy with PerformanceIndex :", round(accuracy * 100, 2), "%")

print("\nObservation:")
print("Compare this accuracy with the previous model.")