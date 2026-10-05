import math

# Actual and predicted values
actual = 1
predicted = 0.8

# Mean Squared Error
mse = (actual - predicted) ** 2

# Binary Cross Entropy
bce = -(actual * math.log(predicted) +
        (1 - actual) * math.log(1 - predicted))

# Display losses
print("Actual Value:", actual)
print("Predicted Value:", predicted)
print("Mean Squared Error:", mse)
print("Binary Cross Entropy:", bce)

print("MSE is mainly used for regression.")
print("Binary Cross Entropy is mainly used for binary classification.")