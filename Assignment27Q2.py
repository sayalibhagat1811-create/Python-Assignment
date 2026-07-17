class BankAccount:
    # Class variable
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display account details
    def Display(self):
        print("\nAccount Holder :", self.Name)
        print("Balance :", self.Amount)

    # Deposit money
    def Deposit(self):
        Dep = float(input("Enter amount to deposit: "))
        self.Amount += Dep
        print("Amount Deposited Successfully.")

    # Withdraw money
    def Withdraw(self):
        Wd = float(input("Enter amount to withdraw: "))
        if Wd <= self.Amount:
            self.Amount -= Wd
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance!")

    # Calculate Interest
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():
    # Object 1
    Obj1 = BankAccount("Sayali", 10000)

    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    Obj1.Display()
    print("Interest =", Obj1.CalculateInterest())

    # Object 2
    Obj2 = BankAccount("Rahul", 5000)

    Obj2.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    Obj2.Display()
    print("Interest =", Obj2.CalculateInterest())


if __name__ == "__main__":
    main()