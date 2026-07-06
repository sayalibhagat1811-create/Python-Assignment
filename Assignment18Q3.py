def Minimum(arr):
    min = arr[0]

    for i in arr:
        if i < min:
            min = i

    return min

n = int(input("Enter number of elements: "))

data = []
for i in range(n):
    no = int(input())
    data.append(no)

print("Minimum number is:", Minimum(data))