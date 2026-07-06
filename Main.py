import Arithmetic

def main():
    value1 = int(input("Enter first number:"))
    value2 = int(input("Enter second number:"))

    print("Addition is:",Arithmetic.Add(value1,value2))
    print("Subtraction is:",Arithmetic.Sub(value1,value2))
    print("Multiplication is:",Arithmetic.Mult(value1,value2))
    print("Division is:",Arithmetic.Div(value1,value2))

if __name__ == "__main__":
    main()