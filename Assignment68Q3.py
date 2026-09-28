# 3. Flattening

matrix = [
    [6, 4],
    [8, 6]
]

print("Input Matrix:")
for row in matrix:
    print(row)

flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("Flatten Output:")
print(flatten_output)

weights = [0.1, 0.2, 0.3, 0.4]
bias = 1

output = 0

for i in range(len(flatten_output)):
    output = output + flatten_output[i] * weights[i]

output = output + bias

print("Fully Connected Layer:")
print("Weights:", weights)
print("Bias:", bias)

print("Final Output:")
print(output)