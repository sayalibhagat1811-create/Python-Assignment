import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

depth = [1, 3, None]

for d in depth:

    model = DecisionTreeClassifier(max_depth=d, random_state=42)

    model.fit(X_train, Y_train)

    accuracy = model.score(X_test, Y_test)

    print("Max Depth =", d, "Testing Accuracy =", round(accuracy * 100, 2), "%")