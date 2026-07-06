def AddFactors(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum = sum + i
    return sum

def main():
    value = int(input("Enter number: "))
    print("Addition of factors =", AddFactors(value))

if __name__ == "__main__":
    main()