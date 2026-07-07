import threading

def CheckPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def Prime(Data):
    print("Prime Numbers :")
    for i in Data:
        if CheckPrime(i):
            print(i)

def NonPrime(Data):
    print("Non Prime Numbers :")
    for i in Data:
        if not CheckPrime(i):
            print(i)

def main():
    Data = [2, 10, 11, 15, 17, 20, 23, 30]

    T1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    T2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()