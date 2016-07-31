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

