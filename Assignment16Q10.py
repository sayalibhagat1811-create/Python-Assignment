def NameLength(name):
    return len(name)

def main():
    name = input("Enter name: ")
    ans = NameLength(name)
    print("Length of name is:", ans)

if __name__ == "__main__":
    main()