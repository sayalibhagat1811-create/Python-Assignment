def CheckDivisible(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

num = int(input("Enter a number: "))

CheckDivisible(num)