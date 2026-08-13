import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

Border = "-" * 50

# Step 1 : Get Data
print(Border)
print("Step 1 : Get Data")
print(Border)

DataPath = "MarvellousInfosystems_PlayPredictor.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully..")
print("Initial entries from dataset are:")
print(df)

# Step 2 : Clean, Prepare and Manipulate Data
print(Border)
print("Step 2 : Clean, Prepare and Manipulate Data")
print(Border)

WeatherEncoder = LabelEncoder()
TemperatureEncoder = LabelEncoder()
PlayEncoder = LabelEncoder()

df["Wether"] = WeatherEncoder.fit_transform(df["Wether"])
df["Temperature"] = TemperatureEncoder.fit_transform(df["Temperature"])
df["Play"] = PlayEncoder.fit_transform(df["Play"])

print("Data converted into numerical format:")
print(df)

# Step 3 : Train Data
print(Border)
print("Step 3 : Train Data")
print(Border)

X = df[["Wether", "Temperature"]]
Y = df["Play"]

XTrain, XTest, YTrain, YTest = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

K = 3

Model = KNeighborsClassifier(n_neighbors=K)

Model.fit(XTrain, YTrain)

print("KNN model trained successfully..")
print("Value of K:", K)

# Step 4 : Test Data
print(Border)
print("Step 4 : Test Data")
print(Border)

Weather = input("Enter Weather (Sunny/Overcast/Rainy): ")
Temperature = input("Enter Temperature (Hot/Mild/Cool): ")

WeatherValue = WeatherEncoder.transform([Weather])[0]
TemperatureValue = TemperatureEncoder.transform([Temperature])[0]

NewData = pd.DataFrame(
    [[WeatherValue, TemperatureValue]],
    columns=["Wether", "Temperature"]
)

Prediction = Model.predict(NewData)

Result = PlayEncoder.inverse_transform(Prediction)

print("Predicted Result:", Result[0])

# Step 5 : Calculate Accuracy
print(Border)
print("Step 5 : Calculate Accuracy")
print(Border)

def CheckAccuracy(K):
    Model = KNeighborsClassifier(n_neighbors=K)

    Model.fit(XTrain, YTrain)

    YPrediction = Model.predict(XTest)

    Accuracy = accuracy_score(YTest, YPrediction)

    return Accuracy * 100

Accuracy = CheckAccuracy(3)

print("Accuracy for K = 3:", Accuracy, "%")

print(Border)