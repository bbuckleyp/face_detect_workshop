#!/usr/bin/env python

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Create a text/plain message
msg = MIMEText("Face detected!")
msg['Subject'] = ""
msg['From'] = "buckey101@gmail.com"
msg['To'] = "8587355592@tmomail.net"

# Send the message via our own SMTP server (sendmail)
s = smtplib.SMTP('localhost')
s.set_debuglevel(1)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()
print "Text message sent!"
