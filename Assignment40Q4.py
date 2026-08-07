import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,Y_train)

students = pd.DataFrame({
    "StudyHours":[6,4,8,3,5],
    "Attendance":[85,70,95,60,88],
    "PreviousScore":[66,50,90,45,72],
    "AssignmentsCompleted":[7,4,10,3,8],
    "SleepHours":[7,6,8,5,7]
})

prediction = model.predict(students)

students["Prediction"] = prediction

students["Prediction"] = students["Prediction"].map({1:"Pass",0:"Fail"})

print(students)