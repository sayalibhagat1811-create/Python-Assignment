from multiprocessing import Pool

def sum_odd(n):
    total = 0

    for i in range(1, n + 1, 2):
        total += i

    return total

def main():
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(sum_odd, data)

    print("Number\tSum of Odd Numbers")
    print("-" * 35)

    for n, total in zip(data, result):
        print(f"{n}\t{total}")

if __name__ == "__main__":
    main()