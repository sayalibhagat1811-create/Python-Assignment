import schedule
import time
import os

def ReadFile(path):
    try:
        file = open(path, "r")
        data = file.read()

        if data == "":
            print("File is empty")
        else:
            print(data)

        file.close()

    except FileNotFoundError:
        print("File does not exist")
    except PermissionError:
        print("Permission denied")
    except:
        print("File cannot be opened")

def main():
    path = input("Enter file path: ")

    schedule.every(1).minutes.do(ReadFile, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()