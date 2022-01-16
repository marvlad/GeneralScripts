# ==========================================================
# Script to check the BNB beam
# For ANNIE Experiment
# Author: M. Ascencio
# Jan 16, 2022

import urllib.request
from bs4 import *
import pyttsx3
import sched, time
from twisted.internet import task, reactor
import smtplib, ssl
from email.message import EmailMessage
from datetime import datetime

# Check the page every `timeout` seconds
timeout = 3.0

def doWork():
    my_request = urllib.request.urlopen("[add here the webpage]")
    my_HTML = my_request.read().decode("utf8")
    soup = BeautifulSoup(my_HTML, "lxml")
    data = pyttsx3.init()
    data.setProperty("rate", 140)
    value = soup.find("td", text="Booster Beam").find_next_sibling("td").string
    BNBInt = float(value)
    alarm_message = "ALERT! BNB beam down!"
    email_message = "The beam is dowm. The intensity value is: "+value+". Date: "

    if BNBInt < 4.22 :

        # Voice alarm
        data.say(alarm_message)
        data.runAndWait()

        #Get current date and time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        email_message = email_message+dt_string
        print(email_message)
        context=ssl.create_default_context()
        '''
        # Preparing info to send by email
        msg = EmailMessage()
        msg.set_content(email_message)
        msg["Subject"] = "ALERT BNB beam down"
        msg["From"] = "[add here an email]"
        msg["To"] = "[add here the email address to send the alert]"

        context=ssl.create_default_context()

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(msg["From"], "[add password]")
            smtp.send_message(msg)
        '''

    print(BNBInt)
    pass

l = task.LoopingCall(doWork)
l.start(timeout) 

reactor.run()

