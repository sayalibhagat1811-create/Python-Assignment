def ChkNum(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    value = int(input("Enter number:"))
    ChkNum(value)

if __name__ == "__main__":
    main()