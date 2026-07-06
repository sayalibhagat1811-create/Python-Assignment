def ListSum(arr):
    total = 0
    for i in arr:
        total = total + i
    return total
n = int(input("Enter number of elements: "))

data = []
for i in range(n):
    no = int(input())
    data.append(no)
print("Addition is:", ListSum(data))

