import numpy as np
import matplotlib.pyplot as plt

# Input values from -10 to 10
x = np.linspace(-10, 10, 100)

# Sigmoid function
sigmoid = 1 / (1 + np.exp(-x))

# ReLU function
relu = np.maximum(0, x)

# Tanh function
tanh = np.tanh(x)

# Plot Sigmoid
plt.plot(x, sigmoid, label="Sigmoid")

# Plot ReLU
plt.plot(x, relu, label="ReLU")

# Plot Tanh
plt.plot(x, tanh, label="Tanh")

plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Activation Functions")
plt.legend()
plt.grid()
plt.show()