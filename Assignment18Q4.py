def Frequency(arr, value):
    count = 0

    for i in arr:
        if i == value:
            count = count + 1

    return count

n = int(input("Enter number of elements: "))

data = []
for i in range(n):
    no = int(input())
    data.append(no)

search = int(input("Enter number to search: "))

print("Frequency is:", Frequency(data, search))