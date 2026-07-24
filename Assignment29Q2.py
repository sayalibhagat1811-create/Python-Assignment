def main():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()