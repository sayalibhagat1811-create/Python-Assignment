def CountLine(filename):
    try:
        with open(filename, "r") as fobj:
            count = 0

            for line in fobj:

                count += 1

            print("total number of lines in", filename,"is:", count)

    except FileNotFoundError:
        print("File is not present in current directory")

def main():
    name = input("Enter file name: ")
    CountLine(name)

if __name__ == "__main__":
    main()    