def Factors(no):
    for i in range(1, no + 1):
        if no % i == 0:
            print(i, end=" ")

num = int(input("Enter number: "))
Factors(num)