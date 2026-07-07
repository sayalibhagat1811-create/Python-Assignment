def main():
    Power = lambda No: No ** 2

    Value = int(input("Enter the number : "))

    Ret = Power(Value)

    print(f"Power of {Value} is {Ret}")

if __name__ == "__main__":
    main()