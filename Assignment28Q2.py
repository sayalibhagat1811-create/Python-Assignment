def CountWords(filename):
    try:
        with open(filename, "r") as fobj:
            data = fobj.read()

            words = data.split()

            print("Total number of words in", filename, "is:", len(words))

    except FileNotFoundError:
        print("File is not present in current directory")


def main():
    name = input("Enter file name: ")
    CountWords(name)


if __name__ == "__main__":
    main()