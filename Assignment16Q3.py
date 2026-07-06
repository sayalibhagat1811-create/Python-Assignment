def Add(NO1, No2):
    return  NO1 + No2
    

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    Ans = Add(value1, value2)
    print("Addition is:", Ans)

if __name__ == "__main__":
    main()