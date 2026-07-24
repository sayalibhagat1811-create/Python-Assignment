def main():
    filename = input("Enter file name: ")
    word = input("Enter string: ")

    try:
        file = open(filename, "r")
        data = file.read()
        file.close()

        count = data.count(word)

        print("Frequency:", count)

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()