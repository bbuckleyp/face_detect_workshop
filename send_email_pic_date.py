#!/usr/bin/env python

import smtplib # Import smtplib for the actual sending email function 
import time    # import time module to create a timestamp


# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Create a multipart message
msg = MIMEMultipart()
msg.attach(MIMEText("Face detected!"))
msg['Subject'] = "Your DB410c has detected someone (%s)" \
        %time.strftime("%m/%d/%Y %H:%M")
msg['From'] = "linaro@localhost"
msg['To'] = "buckley101@gmail.com"

# Try opening and attaching the image file
try:
    f = open("output.jpg", "rb")
    img = MIMEImage(f.read())
    f.close()
    msg.attach(img)
except IOError:
    print "Error: Cannot find 'output.jpg'!"

# Send the message via our own SMTP server (sendmail)
s = smtplib.SMTP('localhost')
s.set_debuglevel(1)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()
print "Email sent!"
