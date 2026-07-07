import threading

def Maximum(Data):
    print("Maximum Element :", max(Data))

def Minimum(Data):
    print("Minimum Element :", min(Data))

def main():
    Data = []

    Size = int(input("Enter number of elements : "))

    print("Enter Elements :")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    T1 = threading.Thread(target=Maximum, args=(Data,))
    T2 = threading.Thread(target=Minimum, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()