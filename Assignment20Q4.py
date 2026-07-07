import threading

def Small(Str):
    Count = 0
    for ch in Str:
        if ch.islower():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small letters :", Count)

def Capital(Str):
    Count = 0
    for ch in Str:
        if ch.isupper():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital letters :", Count)

def Digits(Str):
    Count = 0
    for ch in Str:
        if ch.isdigit():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", Count)

def main():
    Value = input("Enter String : ")

    T1 = threading.Thread(target=Small, args=(Value,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()