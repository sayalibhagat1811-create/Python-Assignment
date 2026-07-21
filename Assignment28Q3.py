def DisplayFile(filename):
    try:
        with open(filename, "r") as fobj:
            for line in fobj:
                print(line, end="")

    except FileNotFoundError:
        print("File is not present in current directory")


def main():
    name = input("Enter file name: ")
    DisplayFile(name)


if __name__ == "__main__":
    main()