import MarvellousNum

def ListPrime(arr):
    total = 0

    for i in arr:
        if MarvellousNum.ChkPrime(i):
            total = total + i

    return total

n = int(input("Enter number of elements: "))

data = []
for i in range(n):
    no = int(input())
    data.append(no)

print("Addition of prime numbers:", ListPrime(data))