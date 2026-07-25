# ---------------------------------------------------------------
# Python Automation Project
# ---------------------------------------------------------------

import os
import sys
import hashlib
import shutil
import smtplib
import time
from datetime import datetime
from email.message import EmailMessage

# ---------------------------------------------------------------
# Display Help

def DisplayHelp():
    print("""
Usage :
python DuplicateFileRemoval.py <Directory> <TimeIntervalInMinutes>

Example :
python DuplicateFileRemoval.py C:\\Demo 30

Description :
This application finds duplicate files using MD5 hash,
deletes duplicate files, generates a log file,
and sends the log through email.
""")

# ---------------------------------------------------------------
# Display Usage

def DisplayUsage():
    print("python DuplicateFileRemoval.py Directory TimeInterval")

# ---------------------------------------------------------------
# Calculate MD5 Hash


def CalculateChecksum(path):

    hobj = hashlib.md5()

    file = open(path,"rb")

    buffer = file.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = file.read(1024)

    file.close()

    return hobj.hexdigest()

# ---------------------------------------------------------------
# Scan Directory

def FindDuplicate(path):

    duplicate = {}

    if not os.path.exists(path):
        print("Directory not found")
        return duplicate

    for FolderName,SubFolder,FileNames in os.walk(path):

        for fname in FileNames:

            filepath = os.path.join(FolderName,fname)

            try:
                checksum = CalculateChecksum(filepath)

                if checksum in duplicate:
                    duplicate[checksum].append(filepath)
                else:
                    duplicate[checksum] = [filepath]

            except Exception:
                pass

    return duplicate

# ---------------------------------------------------------------
# Delete Duplicate Files

def DeleteDuplicateFiles(data):

    count = 0

    deleted = []

    for value in data.values():

        if len(value) > 1:

            for file in value[1:]:

                try:
                    os.remove(file)
                    deleted.append(file)
                    count += 1
                except Exception:
                    pass

    return count, deleted

# ---------------------------------------------------------------
# Create Log File

def CreateLog(deletedfiles):

    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")

    filename = "MarvellousLog_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"

    filepath = os.path.join("Marvellous", filename)

    with open(filepath, "w") as f:

        f.write("--------------------------------------------------\n")
        f.write("Duplicate File Removal Log\n")
        f.write("--------------------------------------------------\n")
        f.write("Time : " + str(datetime.now()) + "\n\n")

        if len(deletedfiles) == 0:
            f.write("No Duplicate Files Found\n")
        else:
            f.write("Deleted Files\n\n")

            for file in deletedfiles:
                f.write(file + "\n")

    return filepath

# ---------------------------------------------------------------
# Send Email

def SendMail(receiver, logfile):
    sender = "sayali123@gmail.com"
    password = "abcd efgh ijkl mnop"
   
    try:
        msg = EmailMessage()

        msg["Subject"] = "Duplicate File Removal Report"
        msg["From"] = sender
        msg["To"] = receiver

        msg.set_content("Please find the attached log file.")

        with open(logfile, "rb") as f:
            data = f.read()
            name = os.path.basename(logfile)

        msg.add_attachment(
            data,
            maintype="application",
            subtype="octet-stream",
            filename=name
        )

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()

        print("Email sent successfully.")

    except Exception as e:
        print("Unable to send email :", e)

# ---------------------------------------------------------------
# Process Directory

def ProcessDirectory(path, receiver):

    print("-------------------------------------")
    print("Searching Duplicate Files...")
    print("-------------------------------------")

    data = FindDuplicate(path)

    deletedCount, deletedFiles = DeleteDuplicateFiles(data)

    logfile = CreateLog(deletedFiles)

    print("Duplicate Files Deleted :", deletedCount)
    print("Log File :", logfile)

    SendMail(receiver, logfile)

# ---------------------------------------------------------------
# Scheduler

def Scheduler(path, interval, receiver):

    while True:

        print("\n")
        print("--------------------------------")
        print("Execution Time :", datetime.now())
        print("--------------------------------")

        ProcessDirectory(path, receiver)

        print("Waiting for next execution...")
        time.sleep(interval * 60)

# ---------------------------------------------------------------
# Main Function

def main():

    print("------------------------------------------------")
    print("        Duplicate File Removal Project")
    print("------------------------------------------------")

    if (len(sys.argv) == 2):

        if (sys.argv[1] == "--help"):
            DisplayHelp()
            return

        elif (sys.argv[1] == "--usage"):
            DisplayUsage()
            return

        else:
            print("Invalid option.")
            DisplayUsage()
            return

    elif (len(sys.argv) != 4):

        print("Invalid number of arguments.")
        DisplayUsage()
        return

    directory = sys.argv[1]

    try:
        interval = int(sys.argv[2])
    except ValueError:
        print("Time interval must be an integer.")
        return

    receiver = sys.argv[3]

    if not os.path.isdir(directory):
        print("Error: Directory does not exist.")
        return

    try:
        Scheduler(directory, interval, receiver)

    except KeyboardInterrupt:
        print("\nApplication terminated by user.")

    except Exception as e:
        print("Error :", e)

# ---------------------------------------------------------------
# Entry Point


if __name__ == "__main__":
    main()