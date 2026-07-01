def Table(no):
    for i in range(1, 11):
        print(no * i, end=" ")

num = int(input("Enter number: "))
Table(num)