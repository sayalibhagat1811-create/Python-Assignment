import psutil
import os
import time
import sys
import smtplib
from email.message import EmailMessage

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

    return filename

def SendMail(receiver, filename):
    sender = "yourgmail@gmail.com"
    password = "your_app_password"

    msg = EmailMessage()
    msg["Subject"] = "Process Log File"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("Please find attached process log file.")

    with open(filename, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(filename)
        )

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()

    print("Mail sent successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python ProcInfoLog.py Demo abc@gmail.com")
        exit()

    logfile = CreateLog(sys.argv[1])
    SendMail(sys.argv[2], logfile)