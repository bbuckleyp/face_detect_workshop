#!/usr/bin/env python

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Create a text/plain message
msg = MIMEText("Face detected!")
msg['Subject'] = "Your DB410c has detected someone"
msg['From'] = "linaro@localhost"
msg['To'] = "buckley101@gmail.com"

# Send the message via our own SMTP server (sendmail)
s = smtplib.SMTP('localhost')
s.set_debuglevel(1)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()
print "Email sent!"
