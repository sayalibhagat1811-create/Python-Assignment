import schedule
import time
import shutil
import os
from datetime import datetime

def Backup():
    source = input("Enter source file: ")
    destination = input("Enter destination folder: ")

    filename = os.path.basename(source)
    name, ext = os.path.splitext(filename)

    newfile = name + "_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ext

    shutil.copy(source, os.path.join(destination, newfile))

    log = open("backup_log.txt", "a")
    log.write("Backup completed at " + str(datetime.now()) + "\n")
    log.close()

    print("Backup Successful")

def main():
    schedule.every().hour.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()