class Arithmetic:
    # Constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Accept values from user
    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))
  
    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not possible."
        return self.Value1 / self.Value2

def main():
    # Object 1
    Obj1 = Arithmetic()
    Obj1.Accept()

    print("\nAddition =", Obj1.Addition())
    print("Subtraction =", Obj1.Subtraction())
    print("Multiplication =", Obj1.Multiplication())
    print("Division =", Obj1.Division())

    # Object 2
    Obj2 = Arithmetic()
    Obj2.Accept()

    print("\nAddition =", Obj2.Addition())
    print("Subtraction =", Obj2.Subtraction())
    print("Multiplication =", Obj2.Multiplication())
    print("Division =", Obj2.Division())

if __name__ == "__main__":
    main()