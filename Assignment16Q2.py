def ChkNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number") 

def main():
    value = int(input("enter the number:"))

    ChkNum(value)

if __name__ == "__main__":
    main()