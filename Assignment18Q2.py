def Maximum(arr):
    max = arr[0]

    for i in arr:
        if i > max:
            max = i

    return max

n = int(input("Enter number of elements: "))

data = []
for i in range(n):
    no = int(input())
    data.append(no)

print("Maximum number is:", Maximum(data))