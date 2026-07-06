def SumDigits(no):
    sum = 0
    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10
    return sum

def main():
    value = int(input("Enter number: "))
    print("Addition of digits =", SumDigits(value))

if __name__ == "__main__":
    main()