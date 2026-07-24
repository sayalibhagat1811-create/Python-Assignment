import schedule
import time
import os
from datetime import datetime

def Scan(path):
    files = 0
    folders = 0

    for item in os.listdir(path):
        fullpath = os.path.join(path, item)

        if os.path.isfile(fullpath):
            files += 1
        elif os.path.isdir(fullpath):
            folders += 1

    print("Directory:", path)
    print("Files:", files)
    print("Subdirectories:", folders)
    print("Scan Time:", datetime.now())

def main():
    path = input("Enter directory path: ")

    schedule.every(1).minutes.do(Scan, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()