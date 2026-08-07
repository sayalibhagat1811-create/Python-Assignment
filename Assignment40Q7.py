import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = df["FinalResult"]

states = [0, 10, 42]

for state in states:

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=state
    )

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(Y_test, prediction)

    print("Random State =", state,
          " Accuracy =", round(accuracy * 100, 2), "%")