def Display(no):
    for i in range(no, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    value = int(input("Enter number: "))
    Display(value)

if __name__ == "__main__":
    main()