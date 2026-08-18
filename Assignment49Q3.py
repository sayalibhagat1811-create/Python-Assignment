import numpy as np

from sklearn.preprocessing import StandardScaler

Data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])
# Create the dataset

Scaler = StandardScaler()
# Create a StandardScaler object

ScaledData = Scaler.fit_transform(Data)
# Fit the scaler and transform the dataset

print("Original Dataset :")
print(Data)

print("Scaled Dataset :")
print(ScaledData)
