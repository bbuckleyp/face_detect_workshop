#!/usr/bin/env python

import cv2, sys

# Define constants
DEVICE_NUMBER = 1
FONT_FACES = [
        cv2.FONT_HERSHEY_SIMPLEX,
        cv2.FONT_HERSHEY_PLAIN,
        cv2.FONT_HERSHEY_DUPLEX,
        cv2.FONT_HERSHEY_COMPLEX,
        cv2.FONT_HERSHEY_TRIPLEX,
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
        cv2.FONT_HERSHEY_SCRIPT_COMPLEX
]

# Initialize webcam
vc = cv2.VideoCapture(DEVICE_NUMBER)

# Check if the webcame works
if vc.isOpened():
    # Try to get the first frame
    retval, frame = vc.read()
else: 
    # Exit the program
    sys.exit(1)

# If the webcam read is successful, loop indefinitely
while retval:
    # Convert frame to grayscale to wipe out color data
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert back to color (to use color text)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

    # Write text onto the frame using a single font
    font_typeface = FONT_FACES[5]
    font_scale = 2
    font_color = (0,0,255)
    font_weight = 5
    x = 0
    y = 50
    cv2.putText(frame, "[LIVE]", (x,y), font_typeface, font_scale, font_color, font_weight)

    # Show the frame on the screen
    cv2.imshow("DB410c Workshop", frame)

    # Read in the next frame
    retval, frame = vc.read()

    # Exit program if the ESCAPE key is pressed
    if cv2.waitKey(1) == 27:
        break
