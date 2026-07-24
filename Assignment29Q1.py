import os

def main():
    filename = input("Enter file name: ")

    if os.path.exists(filename):
        print("File exists")
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()