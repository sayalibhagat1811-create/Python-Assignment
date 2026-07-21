def SearchWord(filename, word):
    try:
        with open(filename, "r") as fobj:
            data = fobj.read()

            if word in data:
                print(word, "is found in", filename)
            else:
                print(word, "is not found in", filename)

    except FileNotFoundError:
        print("File is not present in current directory")


def main():
    name = input("Enter file name: ")
    word = input("Enter word to search: ")

    SearchWord(name, word)


if __name__ == "__main__":
    main()