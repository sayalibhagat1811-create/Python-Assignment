# Input value
x = 2

# Initial weight
weight = 0.5

# Bias
bias = 0.1

# Target output
target = 1

# Learning rate
learning_rate = 0.1

# Calculate prediction
prediction = (x * weight) + bias

# Calculate error
error = target - prediction

# Store old weight
old_weight = weight

# Update weight using gradient descent
weight = weight + (learning_rate * error * x)

# Display results
print("Prediction:", prediction)
print("Error:", error)
print("Old Weight:", old_weight)
print("Updated Weight:", weight)