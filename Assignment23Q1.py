from multiprocessing import Pool

def sum_even(n):
    total = 0

    for i in range(2, n + 1, 2):
        total += i

    return total

def main():
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(sum_even, data)

    print("Number\tSum of Even Numbers")
    print("-" * 35)

    for n, total in zip(data, result):
        print(f"{n}\t{total}")

if __name__ == "__main__":
    main()