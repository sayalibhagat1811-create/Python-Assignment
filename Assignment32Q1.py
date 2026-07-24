import schedule
import time
from datetime import datetime

def CreateFile():
    filename = "File_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    file = open(filename, "w")
    file.write("Filename : " + filename + "\n")
    file.write("Creation Date : " + datetime.now().strftime("%d-%m-%Y") + "\n")
    file.write("Creation Time : " + datetime.now().strftime("%H:%M:%S"))
    file.close()

    print("File Created")

def main():
    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()