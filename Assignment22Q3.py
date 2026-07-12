from multiprocessing import Pool

def count_primes(n):
    count = 0

    for num in range(2, n + 1):
        prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break

        if prime:
            count += 1

    return count

def main():
    numbers = [10000, 20000, 30000, 40000]

    with Pool() as p:
        result = p.map(count_primes, numbers)

    print("Number\tPrime Count")
    print("-" * 25)

    for n, count in zip(numbers, result):
        print(f"{n}\t{count}")

if __name__ == "__main__":
    main()