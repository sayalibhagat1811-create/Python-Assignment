import math

Border = "-" * 40

Data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]

print(Border)
print("KNN Student Result Prediction")
print(Border)

StudyHours = float(input("Enter Study Hours: "))
Attendance = float(input("Enter Attendance: "))

Distances = []

for Hours, Attend, Result in Data:
    Distance = math.sqrt(
        (StudyHours - Hours) ** 2 +
        (Attendance - Attend) ** 2
    )

    Distances.append((Distance, Result))

Distances.sort(key=lambda Item: Item[0])

K = 3
Nearest = Distances[:K]

Votes = {}

for Distance, Result in Nearest:
    Votes[Result] = Votes.get(Result, 0) + 1

PredictedResult = max(Votes, key=Votes.get)

print(Border)
print("Predicted Result:", PredictedResult)
print(Border)