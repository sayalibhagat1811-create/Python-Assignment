class Circle:
    # Class variable
    PI = 3.14

    # Constructor 
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Accept radius from user
    def Accept(self):
        self.Radius = float(input("Enter the radius: "))

    # Calculate area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    # Calculate circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # Display details
    def Display(self):
        print("\nRadius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)


def main():
    # Object 1
    Obj1 = Circle()
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    # Object 2
    Obj2 = Circle()
    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()


if __name__ == "__main__":
    main()