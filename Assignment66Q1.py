import math

# Input values
x1 = 2
x2 = 3

# Weights
w1 = 0.4
w2 = 0.6

# Bias
bias = 0.5

# Calculate weighted sum
weighted_sum = (x1 * w1) + (x2 * w2) + bias

# Apply sigmoid activation function
output = 1 / (1 + math.exp(-weighted_sum))

# Display results
print("Weighted Sum:", weighted_sum)
print("Final Output:", output)

# Check whether output is close to 0 or 1
if output >= 0.5:
    print("Output is close to 1")
else:
    print("Output is close to 0")