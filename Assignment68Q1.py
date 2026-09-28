# 1. Manual Convolution

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]

feature_map = []

print("Input Image:")
for row in image:
    print(row)

print("Kernel:")
for row in kernel:
    print(row)

print("Region Calculations:")

for i in range(3):
    row_output = []

    for j in range(3):
        region = [
            image[i][j:j+3],
            image[i+1][j:j+3],
            image[i+2][j:j+3]
        ]

        result = 0

        for x in range(3):
            for y in range(3):
                result = result + region[x][y] * kernel[x][y]

        print("Region:")
        for row in region:
            print(row)

        print("Output =", result)

        row_output.append(result)

    feature_map.append(row_output)

print("Feature Map:")
for row in feature_map:
    print(row)