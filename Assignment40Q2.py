import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

# Full Model
X1 = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X1, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

pred = model.predict(X_test)

acc1 = accuracy_score(Y_test,pred)

# Remove SleepHours
X2 = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted"]]

X_train, X_test, Y_train, Y_test = train_test_split(
    X2, Y, test_size=0.2, random_state=42
)

model.fit(X_train,Y_train)

pred = model.predict(X_test)

acc2 = accuracy_score(Y_test,pred)

print("Accuracy with SleepHours :", round(acc1*100,2),"%")
print("Accuracy without SleepHours :", round(acc2*100,2),"%")