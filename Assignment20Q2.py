import threading

def EvenFactor(No):
    Sum = 0
    print("Even Factors:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i)
            Sum = Sum + i

    print("Sum of Even Factors :", Sum)

def OddFactor(No):
    Sum = 0
    print("Odd Factors:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i)
            Sum = Sum + i

    print("Sum of Odd Factors :", Sum)

def main():
    Value = int(input("Enter number : "))

    T1 = threading.Thread(target=EvenFactor, args=(Value,), name="EvenFactor")
    T2 = threading.Thread(target=OddFactor, args=(Value,), name="OddFactor")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()