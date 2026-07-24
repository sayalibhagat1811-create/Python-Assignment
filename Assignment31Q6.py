import schedule
import time

def Monday():
    print("Start your weekly goals")

def Wednesday():
    print("Review your weekly progress")

def Friday():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(Monday)
    schedule.every().wednesday.at("17:00").do(Wednesday)
    schedule.every().friday.at("18:00").do(Friday)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()