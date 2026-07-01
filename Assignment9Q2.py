def ChkGreater(no1, no2):
    if no1 > no2:
        print("Greater number is:", no1)
    elif no2 > no1:
        print("Greater number is:", no2)
    else:
        print("Both numbers are equal")



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


ChkGreater(num1, num2)