import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

train_accuracy = model.score(X_train, Y_train)

test_accuracy = model.score(X_test, Y_test)

print("Training Accuracy =", round(train_accuracy * 100, 2), "%")

print("Testing Accuracy =", round(test_accuracy * 100, 2), "%")

if train_accuracy > test_accuracy:
    print("Model may be Overfitting")
elif train_accuracy < test_accuracy:
    print("Model may be Underfitting")
else:
    print("Model is Balanced")