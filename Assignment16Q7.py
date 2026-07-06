def ChkDiv(no):
    if no % 5 == 0:
        return True
    else:
        return False
    
def main():
    value = int(input("enter number:"))
    ans = ChkDiv(value)
    print(ans)

if __name__ == "__main__":
    main()