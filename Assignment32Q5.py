import schedule
import time
import os

def DeleteEmpty(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)

            try:
                if os.path.getsize(filepath) == 0:
                    os.remove(filepath)
                    print("Deleted:", filepath)
            except:
                print("Permission Denied")

def main():
    path = input("Enter Directory Path: ")

    schedule.every().hour.do(DeleteEmpty, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()