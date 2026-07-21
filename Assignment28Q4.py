def CopyFile(source, destination):
    try:
        with open(source, "r") as fsrc:
            data = fsrc.read()

        with open(destination, "w") as fdest:
            fdest.write(data)

        print("Contents of", source, "copied into", destination)

    except FileNotFoundError:
        print("Source file is not present in current directory")


def main():
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    CopyFile(source, destination)


if __name__ == "__main__":
    main()