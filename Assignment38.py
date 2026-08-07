import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. Load Dataset
# -------------------------------------------------------------

df = pd.read_csv("student_performance_ml.csv")

print("="*60)
print("First 5 Records")
print("="*60)
print(df.head())

print("\n" + "="*60)
print("Last 5 Records")
print("="*60)
print(df.tail())

print("\nShape of Dataset")
print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# -------------------------------------------------------------
# 2. Total Students, Pass and Fail Count
# -------------------------------------------------------------

print("\n" + "="*60)
print("Student Statistics")
print("="*60)

total_students = len(df)
passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()

print("Total Students :", total_students)
print("Passed :", passed)
print("Failed :", failed)

# -------------------------------------------------------------
# 3. Statistical Calculations
# -------------------------------------------------------------

print("\n" + "="*60)
print("Statistical Analysis")
print("="*60)

print("Average Study Hours :", df["StudyHours"].mean())
print("Average Attendance :", df["Attendance"].mean())
print("Maximum Previous Score :", df["PreviousScore"].max())
print("Minimum Sleep Hours :", df["SleepHours"].min())

# -------------------------------------------------------------
# 4. Distribution of FinalResult
# -------------------------------------------------------------

print("\n" + "="*60)
print("Pass / Fail Distribution")
print("="*60)

result = df["FinalResult"].value_counts()

print(result)

percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("\nPercentage Distribution")
print(percentage)

if abs(percentage[1] - percentage[0]) <= 10:
    print("\nDataset is Balanced.")
else:
    print("\nDataset is Imbalanced.")

# -------------------------------------------------------------
# 5. Analysis
# -------------------------------------------------------------

print("\n" + "="*60)
print("Average Study Hours based on Result")
print("="*60)

print(df.groupby("FinalResult")["StudyHours"].mean())

print("\nAverage Attendance based on Result")
print(df.groupby("FinalResult")["Attendance"].mean())

print("""
Observation:
1. Students with higher StudyHours generally have better chances of passing.
2. Students with higher Attendance usually achieve better FinalResult.
3. Regular attendance improves classroom understanding.
4. Consistent study and attendance together improve academic performance.
5. Study habits and attendance both influence success.
""")

# -------------------------------------------------------------
# 6. Histogram of StudyHours
# -------------------------------------------------------------

plt.figure(figsize=(6,5))
plt.hist(df["StudyHours"], bins=10)
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

print("""
Histogram Observation:
The histogram shows how study hours are distributed.
If most students are concentrated in the middle,
the data is normally distributed.
Students studying more hours are expected to perform better.
""")

# -------------------------------------------------------------
# 7. Scatter Plot
# -------------------------------------------------------------

plt.figure(figsize=(6,5))

pass_data = df[df["FinalResult"] == 1]
fail_data = df[df["FinalResult"] == 0]

plt.scatter(pass_data["StudyHours"],
            pass_data["PreviousScore"],
            color="green",
            label="Pass")

plt.scatter(fail_data["StudyHours"],
            fail_data["PreviousScore"],
            color="red",
            label="Fail")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")
plt.legend()
plt.show()

# -------------------------------------------------------------
# 8. Boxplot of Attendance
# -------------------------------------------------------------

plt.figure(figsize=(6,5))
plt.boxplot(df["Attendance"])
plt.title("Attendance Boxplot")
plt.ylabel("Attendance")
plt.show()

print("""
Observation:
Any points outside the whiskers represent outliers.
These students have unusually low or high attendance.
""")

# -------------------------------------------------------------
# 9. Assignments Completed vs FinalResult
# -------------------------------------------------------------

assignment_avg = df.groupby("FinalResult")["AssignmentsCompleted"].mean()

assignment_avg.plot(kind="bar")

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Average Assignments Completed")
plt.xticks([0,1],["Fail","Pass"], rotation=0)
plt.show()

print("""
Observation:
Students who completed more assignments
generally have a higher probability of passing.
Assignment completion reflects consistency.
""")

# -------------------------------------------------------------
# 10. Sleep Hours vs FinalResult
# -------------------------------------------------------------

sleep_avg = df.groupby("FinalResult")["SleepHours"].mean()

sleep_avg.plot(kind="bar")

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Average Sleep Hours")
plt.xticks([0,1],["Fail","Pass"], rotation=0)
plt.show()

print("""
Observation:
Adequate sleep improves concentration and learning.
However, sleeping more alone does not guarantee success.
Study hours, attendance, previous performance,
and assignments also play important roles.
""")