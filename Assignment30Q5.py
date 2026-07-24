import schedule
import time
from datetime import datetime

def WriteFile():
    file = open("Marvellous.txt", "a")
    file.write("Task executed at: " + str(datetime.now()) + "\n")
    file.close()
    print("Data written")

def main():
    schedule.every(5).minutes.do(WriteFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()