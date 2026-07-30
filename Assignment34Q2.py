import psutil
import sys

def ProcessInfo(name):
    found = False

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if proc.info['name'].lower() == name.lower():
                found = True
                print("PID :", proc.info['pid'])
                print("Name :", proc.info['name'])
                print("Username :", proc.info['username'])
                print("-" * 30)
        except:
            pass

    if not found:
        print("Process not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python ProcInfo.py Notepad")
        exit()

    ProcessInfo(sys.argv[1])