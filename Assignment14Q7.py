CheckDivisible = lambda No: (No % 5 == 0)

def main():
    Value = int(input("Enter number : "))

    Ans = CheckDivisible(Value)
    print(Ans)

if __name__ == "__main__":
    main()