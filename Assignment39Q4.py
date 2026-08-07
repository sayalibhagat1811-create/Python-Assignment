import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

prediction = model.predict(X_test)

cm = confusion_matrix(Y_test, prediction)

display = ConfusionMatrixDisplay(cm)

display.plot()

plt.show()

print("True Positive : Correctly Predicted Pass")
print("True Negative : Correctly Predicted Fail")
print("False Positive : Predicted Pass but Actually Fail")
print("False Negative : Predicted Fail but Actually Pass")