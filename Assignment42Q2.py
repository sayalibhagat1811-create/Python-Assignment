import math

Border = "-" * 40

Data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue"),
    ("E", 4, 2, "Blue")
]

print(Border)
print("KNN Prediction for Different K Values")
print(Border)

X = float(input("Enter X coordinate: "))
Y = float(input("Enter Y coordinate: "))

Distances = []

for Point, PX, PY, Label in Data:
    Distance = math.sqrt((X - PX) ** 2 + (Y - PY) ** 2)
    Distances.append((Point, Distance, Label))

Distances.sort(key=lambda Item: Item[1])

KValues = [1, 3, 5]

print(Border)
print("Prediction Results")
print(Border)

for K in KValues:
    Nearest = Distances[:K]

    Votes = {}

    for Point, Distance, Label in Nearest:
        Votes[Label] = Votes.get(Label, 0) + 1

    PredictedClass = max(Votes, key=Votes.get)

    print("K =", K, PredictedClass)

print(Border)