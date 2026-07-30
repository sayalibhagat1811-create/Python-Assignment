import psutil

def ProcessDisplay():
    print("{:<10} {:<30} {:<20}".format("PID", "Name", "Username"))

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            print("{:<10} {:<30} {:<20}".format(
                proc.info['pid'],
                proc.info['name'],
                str(proc.info['username'])
            ))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

if __name__ == "__main__":
    ProcessDisplay()