import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

prediction = model.predict(X_test)

misclassified = X_test.copy()
misclassified["Actual"] = Y_test.values
misclassified["Predicted"] = prediction

misclassified = misclassified[misclassified["Actual"] != misclassified["Predicted"]]

print("Misclassified Students")
print(misclassified)

print("\nTotal Misclassified Students :", len(misclassified))

print("\nObservation:")
print("These students were predicted incorrectly by the model.")
print("They may have mixed feature values, making prediction difficult.")