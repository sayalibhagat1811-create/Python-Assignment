import numpy as np

from sklearn.preprocessing import StandardScaler

Point1 = np.array([25, 20000])
Point2 = np.array([35, 80000])

DistanceBefore = np.linalg.norm(Point1 - Point2)
# Calculate Euclidean distance before scaling

print("Distance Before Scaling :", DistanceBefore)

Data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

Scaler = StandardScaler()
# Create StandardScaler object

ScaledData = Scaler.fit_transform(Data)
# Scale all features

DistanceAfter = np.linalg.norm(ScaledData[0] - ScaledData[2])
# Calculate Euclidean distance after scaling

print("Distance After Scaling :", DistanceAfter)