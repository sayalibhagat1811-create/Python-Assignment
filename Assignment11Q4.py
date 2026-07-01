def Reverse(no):
    rev = 0

    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    return rev

num = int(input("Enter number: "))
print(Reverse(num))