from multiprocessing import Pool
import os

def count_odd(n):
    count = (n + 1) // 2
    return (os.getpid(), n, count)

def main():
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(count_odd, data)

    for pid, num, count in result:
        print("Process ID:", pid)
        print("Input Number:", num)
        print("Odd Number Count:", count)
        print()

if __name__ == "__main__":
    main()