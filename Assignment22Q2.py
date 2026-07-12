from multiprocessing import Pool
import os
import math

def factorial_info(num):
    return (os.getpid(), num, math.factorial(num))

def main():
    numbers = [10, 15, 20, 25]

    with Pool() as p:
        result = p.map(factorial_info, numbers)

    print("Process ID\tInput Number\tFactorial")
    print("-" * 70)

    for pid, num, fact in result:
        print(f"{pid}\t\t{num}\t\t{fact}")

if __name__ == "__main__":
    main()