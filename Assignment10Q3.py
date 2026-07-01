def Factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    return fact

num = int(input("Enter number: "))
print("Factorial =", Factorial(num))