import psutil
import os
import time
import sys

def CreateLog(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    filename = os.path.join(dirname, "ProcessLog.txt")

    with open(filename, "w") as f:
        f.write("Process Information\n")
        f.write(time.ctime() + "\n\n")

        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                f.write(f"PID : {proc.info['pid']}\n")
                f.write(f"Name : {proc.info['name']}\n")
                f.write(f"Username : {proc.info['username']}\n")
                f.write("-" * 40 + "\n")
            except:
                pass

    print("Log file created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python ProcInfoLog.py Demo")
        exit()

    CreateLog(sys.argv[1])