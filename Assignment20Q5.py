import threading

def Thread1():
    print("Numbers from 1 to 50")
    for i in range(1, 51):
        print(i)

def Thread2():
    print("Numbers from 50 to 1")
    for i in range(50, 0, -1):
        print(i)

def main():
    T1 = threading.Thread(target=Thread1, name="Thread1")
    T2 = threading.Thread(target=Thread2, name="Thread2")

    T1.start()
    T1.join()

    T2.start()
    T2.join()

if __name__ == "__main__":
    main()