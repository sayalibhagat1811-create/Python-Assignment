import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,Y_train)

pred = model.predict(X_test)

correct = 0

for actual,predict in zip(Y_test,pred):

    if actual == predict:
        correct += 1

manual_accuracy = correct / len(Y_test)

print("Manual Accuracy :",round(manual_accuracy*100,2),"%")

sklearn_accuracy = accuracy_score(Y_test,pred)

print("Sklearn Accuracy :",round(sklearn_accuracy*100,2),"%")