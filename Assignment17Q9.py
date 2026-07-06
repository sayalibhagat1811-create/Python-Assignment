def CountDigits(no):
    count = 0
    while no > 0:
        count += 1
        no = no // 10
    return count

def main():
    value = int(input("Enter number: "))
    print("Number of digits =", CountDigits(value))

if __name__ == "__main__":
    main()