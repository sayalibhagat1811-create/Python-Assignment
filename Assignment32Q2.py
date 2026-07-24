import schedule
import time
import os
from datetime import datetime

def Monitor(path):
    file = open("FileSizeLog.txt", "a")

    if os.path.exists(path):
        size = os.path.getsize(path)
        file.write(f"{path}  Size: {size} bytes  Time: {datetime.now()}\n")
        print("Size:", size)
    else:
        file.write(f"{path} File Not Found\n")
        print("File Not Found")

    file.close()

def main():
    path = input("Enter file path: ")

    schedule.every(30).seconds.do(Monitor, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()