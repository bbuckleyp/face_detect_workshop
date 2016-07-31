#!/usr/bin/env Python

import cv2, sys, smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Define constants
DEVICE_NUMBER = 1
IMAGE_FILE = "detected_face.jpg",

# Get XML file input
if len(sys.argv) > 1:
    XML_PATH = sys.argv[1]
else:
    print "Error: XML path not definted"
    sys.exit(1)

# Initialize the cascade classifier 
faceCascade = cv2.CascadeClassifier(XML_PATH)

# Initialize webcam
vc = cv2.VideoCapture(DEVICE_NUMBER)

# Check if the webcam works
if vc.isOpen():
    # Try to get the first frame
    retval, frame = vc.read()
else:
    # Exit the program
    sys.exit(1)

i = 0
faces = []

# If the webcam read is successful, loop indefinitely
while retval:
    # Define the frame which the program will show
    frame_show = frame

    if i % 5 == 0:
        # Convert frame to grayscale to perform facial detection
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect objects and return an array of faces
        faces = faceCascade.detectMultiScale(
                frame,
                scaleFactor=1.2,
                minNeighbors=2,
                minSize=(50,50),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
                )

    # If at least one face as been detected
    if len(faces) > 0:
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame_show, (x,y), (x+w, y+h), (0,0,255), 2)

        # save the frame as an image file
        cv2.imwrite(IMAGE_FILE, frame_show)

        # Exit the webcam while-loop
        break
    # show the frame on the screen
    cv2.imshow("DB410c Workshop", frame_show)

    # read in the next frame
    retval, frame = vc.read()

    # exit the webcam while-loop if the ESCAPE key is pressed
    if cv2.waitKey(1) == 27:
        break

    i += 1

# once you have exited the webcam while-loop,
# create an email and try to attach the detect face image
msg = MIMEMultipart()
msg.attach(MIMEText("Face detected!"))
msg['Subject'] = "Your DB410c has detected someone"
msg['From'] = "linaro@localhost"
msg['To'] = "buckley101@gmail.com"

try:
    f = open(IMAGE_FILE, "rb")
    img = MIMEImage(f.read())
    f.close()
    msg.attach(img)
except IOError:
    print "Error: Cannot find", IMAGE_FILE

# Send the message via our own SMTP server (sendmail)
s = smtplib.SMTP('localhost')
s.set_debuglevel(1)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()
print "Email sent!"
