from multiprocessing import Pool
import math
import os

def factorial_num(n):
    return (os.getpid(), n, math.factorial(n))

def main():
    data = [10, 15, 20, 25]

    with Pool() as p:
        result = p.map(factorial_num, data)

    for pid, num, fact in result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Factorial :", fact)
        print()

if __name__ == "__main__":
    main()