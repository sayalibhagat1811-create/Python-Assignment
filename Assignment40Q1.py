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

importance = model.feature_importances_

print("Feature Importance\n")

for feature, score in zip(X.columns, importance):
    print(feature, ":", round(score,4))

max_index = importance.argmax()
min_index = importance.argmin()

print("\nMost Important Feature :", X.columns[max_index])
print("Least Important Feature :", X.columns[min_index])