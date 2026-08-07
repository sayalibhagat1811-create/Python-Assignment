# ------------------------------------------------------------
# Student Performance Prediction using Decision Tree
# Complete Structured Python Program
# ------------------------------------------------------------

# -----------------------------
# Step 1 : Import Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# -----------------------------
# Step 2 : Load Dataset
# -----------------------------
df = pd.read_csv("student_performance_ml.csv")

print("="*50)
print("STUDENT PERFORMANCE DATASET")
print("="*50)

print("\nFirst 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

print("\nDataset Shape :", df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# -----------------------------
# Step 3 : Data Analysis
# -----------------------------
print("\n========== DATA ANALYSIS ==========")

print("Total Students :", len(df))

print("Passed Students :", (df["FinalResult"] == 1).sum())

print("Failed Students :", (df["FinalResult"] == 0).sum())

print("\nAverage Study Hours :", df["StudyHours"].mean())

print("Average Attendance :", df["Attendance"].mean())

print("Maximum Previous Score :", df["PreviousScore"].max())

print("Minimum Sleep Hours :", df["SleepHours"].min())

print("\nPass / Fail Distribution")
print(df["FinalResult"].value_counts())

# -----------------------------
# Step 4 : Visualization
# -----------------------------

# Histogram
plt.figure(figsize=(6,4))
plt.hist(df["StudyHours"], bins=10)

plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()

# Scatter Plot
pass_data = df[df["FinalResult"] == 1]
fail_data = df[df["FinalResult"] == 0]

plt.figure(figsize=(6,4))

plt.scatter(pass_data["StudyHours"],
            pass_data["PreviousScore"],
            color="green",
            label="Pass")

plt.scatter(fail_data["StudyHours"],
            fail_data["PreviousScore"],
            color="red",
            label="Fail")

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.legend()

plt.show()

# Boxplot
plt.figure(figsize=(5,4))

plt.boxplot(df["Attendance"])

plt.title("Attendance Boxplot")
plt.ylabel("Attendance")

plt.show()

# -----------------------------
# Step 5 : Prepare Input & Output
# -----------------------------
X = df[["StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"]]

Y = df["FinalResult"]

# -----------------------------
# Step 6 : Train-Test Split
# -----------------------------
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42
)

print("\nDataset Split Successfully")

# -----------------------------
# Step 7 : Train Model
# -----------------------------
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

print("Decision Tree Model Trained Successfully")

# -----------------------------
# Step 8 : Prediction
# -----------------------------
prediction = model.predict(X_test)

print("\nActual\tPredicted")

for actual, pred in zip(Y_test, prediction):
    print(actual, "\t", pred)

# Predict New Student
student = [[6, 85, 66, 7, 7]]

result = model.predict(student)

print("\nPrediction for New Student")

if result[0] == 1:
    print("Result : PASS")
else:
    print("Result : FAIL")

# -----------------------------
# Step 9 : Accuracy Calculation
# -----------------------------
train_accuracy = model.score(X_train, Y_train)

test_accuracy = model.score(X_test, Y_test)

accuracy = accuracy_score(Y_test, prediction)

print("\nTraining Accuracy :", round(train_accuracy*100,2), "%")

print("Testing Accuracy :", round(test_accuracy*100,2), "%")

print("Accuracy Score :", round(accuracy*100,2), "%")

# -----------------------------
# Step 10 : Confusion Matrix
# -----------------------------
cm = confusion_matrix(Y_test, prediction)

display = ConfusionMatrixDisplay(confusion_matrix=cm)

display.plot()

plt.show()

print("\nConfusion Matrix Explanation")

print("True Positive  : Student Passed and Model Predicted Pass")

print("True Negative  : Student Failed and Model Predicted Fail")

print("False Positive : Model Predicted Pass but Student Failed")

print("False Negative : Model Predicted Fail but Student Passed")

# -----------------------------
# Step 11 : Final Conclusion
# -----------------------------
print("\n========== FINAL CONCLUSION ==========")

print("1. The Decision Tree model was trained successfully.")

print("2. Study Hours, Attendance, Previous Score, Assignment Completion and Sleep Hours affect student performance.")

print("3. The model predicts whether a student will Pass or Fail.")

print("4. Accuracy Score and Confusion Matrix are used to evaluate model performance.")

print("5. Regular study, good attendance and completing assignments increase the chances of passing.")