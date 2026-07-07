import threading

Sum = 0
Product = 1

def Addition(Data):
    global Sum

    for i in Data:
        Sum = Sum + i

def Multiplication(Data):
    global Product

    for i in Data:
        Product = Product * i

def main():
    global Sum, Product

    Data = [2, 3, 4, 5]

    T1 = threading.Thread(target=Addition, args=(Data,))
    T2 = threading.Thread(target=Multiplication, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum :", Sum)
    print("Product :", Product)

if __name__ == "__main__":
    main()