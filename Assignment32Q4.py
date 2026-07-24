import schedule
import time
import shutil
import os

def CopyFiles(src, dest):
    for file in os.listdir(src):
        if file.endswith(".txt"):
            try:
                shutil.copy(os.path.join(src, file), dest)
                print(file, "Copied")
            except:
                print(file, "Not Copied")

def main():
    src = input("Enter Source Folder: ")
    dest = input("Enter Destination Folder: ")

    schedule.every(10).minutes.do(CopyFiles, src, dest)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()