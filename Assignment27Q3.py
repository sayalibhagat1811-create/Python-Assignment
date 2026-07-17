class Numbers:
    # Constructor
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    # Check Prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    # Check Perfect
    def ChkPerfect(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i

        if Sum == self.Value:
            return True
        else:
            return False

    # Display Factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Sum of Factors
    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum += i
        return Sum


def main():
    # Object 1
    Obj1 = Numbers()

    print("\nPrime :", Obj1.ChkPrime())
    print("Perfect :", Obj1.ChkPerfect())
    Obj1.Factors()
    print("Sum of Factors :", Obj1.SumFactors())

    # Object 2
    Obj2 = Numbers()

    print("\nPrime :", Obj2.ChkPrime())
    print("Perfect :", Obj2.ChkPerfect())
    Obj2.Factors()
    print("Sum of Factors :", Obj2.SumFactors())


if __name__ == "__main__":
    main()