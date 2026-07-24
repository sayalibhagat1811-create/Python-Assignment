import sys

def main():
    source = sys.argv[1]

    file1 = open(source, "r")
    data = file1.read()
    file1.close()

    file2 = open("Demo1.txt", "w")
    file2.write(data)
    file2.close()

    print("Contents copied successfully")

if __name__ == "__main__":
    main()