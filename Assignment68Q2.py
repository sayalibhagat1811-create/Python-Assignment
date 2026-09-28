# 2. ReLU and Max Pooling

feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

print("Original Feature Map:")
for row in feature_map:
    print(row)


relu_output = []

for row in feature_map:
    new_row = []

    for value in row:
        if value < 0:
            new_row.append(0)
        else:
            new_row.append(value)

    relu_output.append(new_row)

print("After ReLU:")
for row in relu_output:
    print(row)

pool_size = 2
pooled_output = []

for i in range(0, len(relu_output) - 1, pool_size):
    row_output = []

    for j in range(0, len(relu_output[0]) - 1, pool_size):

        values = [
            relu_output[i][j],
            relu_output[i][j+1],
            relu_output[i+1][j],
            relu_output[i+1][j+1]
        ]

        row_output.append(max(values))

    pooled_output.append(row_output)

print("After 2x2 Max Pooling:")
for row in pooled_output:
    print(row)