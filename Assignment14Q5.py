CheckEven = lambda No: (No % 2 == 0)

def main():
    Value = int(input("Enter number : "))

    Ans = CheckEven(Value)
    print(Ans)

if __name__ == "__main__":
    main()