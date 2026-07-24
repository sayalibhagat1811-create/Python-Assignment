import schedule
import time
import os
from datetime import datetime

def CountFiles(path):
    count = 0

    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            count += 1

    file = open("DirectoryCountLog.txt", "a")
    file.write("Directory: " + path + "\n")
    file.write("Files: " + str(count) + "\n")
    file.write("Time: " + str(datetime.now()) + "\n\n")
    file.close()

    print("Count saved")

def main():
    path = input("Enter directory path: ")

    schedule.every(5).minutes.do(CountFiles, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()