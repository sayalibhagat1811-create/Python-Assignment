Minimum = lambda No1, No2: No1 if No1 < No2 else No2

def main():
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))

    Ans = Minimum(A, B)
    print("Minimum number is :", Ans)

if __name__ == "__main__":
    main()