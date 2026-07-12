from multiprocessing import Pool

def sum_of_fifth_powers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i ** 5)

    return total

def main():
    numbers = [10, 20, 30, 40]

    with Pool() as p:
        result = p.map(sum_of_fifth_powers, numbers)

    print("Number\tSum of 5th Powers")
    print("-" * 35)

    for n, total in zip(numbers, result):
        print(f"{n}\t{total}")

if __name__ == "__main__":
    main()