import threading

Counter = 0
Lock = threading.Lock()

def Increment():
    global Counter

    for i in range(1000):
        Lock.acquire()
        Counter = Counter + 1
        Lock.release()

def main():
    T1 = threading.Thread(target=Increment)
    T2 = threading.Thread(target=Increment)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Final Counter :", Counter)

if __name__ == "__main__":
    main()