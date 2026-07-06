def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def main():
    value = int(input("Enter number: "))
    if ChkPrime(value):
        print("Prime Number")
    else:
        print("Not Prime Number")

if __name__ == "__main__":
    main()