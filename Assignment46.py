import pandas as pd

from sklearn.model_selection import train_test_split
# train_test_split is used to divide the dataset into training and testing data

from sklearn.linear_model import LinearRegression
# LinearRegression is used to create the Linear Regression model

from sklearn.metrics import mean_squared_error, r2_score
# mean_squared_error calculates prediction error
# r2_score calculates the accuracy of the regression model

Border = "-" * 50


############################################
# Step 1 : Get Data
############################################

print(Border)
print("Step 1 : Get Data")
print(Border)

DataPath = "MarvellousAdvertising.csv"

df = pd.read_csv(DataPath)
# read_csv loads the CSV file into a pandas DataFrame

print("Dataset loaded successfully")
print("First 5 records are :")
print(df.head())
# head() displays the first 5 records


############################################
# Step 2 : Clean, Prepare and Manipulate Data
############################################

print(Border)
print("Step 2 : Clean, Prepare and Manipulate Data")
print(Border)

print("Dataset Information :")
print(df.info())
# info() displays information about columns, data types and null values

print("Column Names :")
print(df.columns)
# columns displays all column names

print("Shape of Dataset :")
print(df.shape)
# shape displays number of rows and columns

X = df[["TV", "radio", "newspaper"]]
# X contains the input features used for prediction

Y = df["sales"]
# Y contains the target variable that we want to predict


############################################
# Step 3 : Train Data
############################################

print(Border)
print("Step 3 : Train Data")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)
# train_test_split divides the dataset into 50% training and 50% testing data

print("Training Data :")
print(X_train)
# X_train contains input values for training

print("Testing Data :")
print(X_test)
# X_test contains input values for testing

print("Training Target Data :")
print(Y_train)
# Y_train contains sales values for training

print("Testing Target Data :")
print(Y_test)
# Y_test contains actual sales values for testing

Model = LinearRegression()
# LinearRegression creates the Linear Regression model

Model.fit(X_train, Y_train)
# fit() trains the Linear Regression model using training data


############################################
# Step 4 : Test the Data
############################################

print(Border)
print("Step 4 : Test the Data")
print(Border)

Y_pred = Model.predict(X_test)
# predict() predicts sales values using the testing data

print("Actual Sales Values :")
print(Y_test.values)
# Displays the actual sales values

print("Predicted Sales Values :")
print(Y_pred)
# Displays the sales values predicted by the Linear Regression model


############################################
# Step 5 : Display Predicted Values
############################################

print(Border)
print("Step 5 : Display Predicted Values")
print(Border)

Result = pd.DataFrame({
    "Actual Sales": Y_test.values,
    "Predicted Sales": Y_pred
})
# DataFrame creates a table containing actual and predicted sales values

print(Result)
# Displays actual and predicted sales values


############################################
# Model Performance
############################################

print(Border)
print("Model Performance")
print(Border)

MSE = mean_squared_error(Y_test, Y_pred)
# mean_squared_error calculates the Mean Squared Error

R2 = r2_score(Y_test, Y_pred)
# r2_score calculates the R-squared score

print("Mean Squared Error :", MSE)
print("R2 Score :", R2)

print(Border)