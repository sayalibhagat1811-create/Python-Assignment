def Odd(no):
    for i in range(1, no + 1, 2):
        print(i, end=" ")

num = int(input("Enter number: "))
Odd(num)