import math

Border = "-" * 40

Data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

print(Border)
print("K-Nearest Neighbors Classification")
print(Border)

X = float(input("Enter X coordinate: "))
Y = float(input("Enter Y coordinate: "))

Distances = []

for Point, PX, PY, Label in Data:
    Distance = math.sqrt((X - PX) ** 2 + (Y - PY) ** 2)
    Distances.append((Point, Distance, Label))

Distances.sort(key=lambda Item: Item[1])

K = 3
Nearest = Distances[:K]

print(Border)
print("Nearest Neighbors:")
print(Border)

for Point, Distance, Label in Nearest:
    print(Point, "Distance:", round(Distance, 2))

Votes = {}

for Point, Distance, Label in Nearest:
    Votes[Label] = Votes.get(Label, 0) + 1

PredictedClass = max(Votes, key=Votes.get)

print(Border)
print("Predicted Class:")
print(PredictedClass)
print(Border)