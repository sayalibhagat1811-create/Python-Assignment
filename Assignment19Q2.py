def main():
    Mult = lambda No1, No2, : No1 * No2
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))

    Ret = Mult(Value1, Value2)

    print(f"Multipication is {Ret}")

if __name__ == "__main__":
    main()