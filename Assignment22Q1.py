from multiprocessing import Pool
def SumSquares(n):
    return n *(n + 1) * (2 * n + 1) // 6

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        result = pool.map(SumSquares, numbers)

    print("Input :", numbers)
    print("Output:", result)

if __name__ == "__main__":
    main()