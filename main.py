# import the necessary packages
from datetime import datetime

import cv2
#(, cv2.CAP_DSHOW)
# grab a pointer to the video stream and initialize the FPS counter
import torch as torch

print("[INFO] sampling frames from webcam...")
stream = cv2.VideoCapture('1.mov')
start1 = datetime.now()
# loop over some frames
counter_fps1 = 0
while True:
    # grab the frame from the stream and resize it to have a maximum
    # width of 400 pixels
    (grabbed, frame1) = stream.read()
    if not grabbed:
        break
    # frame1 = imutils.resize(frame1, width=1000)
    cv2.imshow("window_name", frame1)
    counter_fps1 = counter_fps1 + 1
    end1 = datetime.now()
    elasped1 = (end1 - start1).total_seconds()
    if cv2.waitKey(1) == 27 or elasped1 >= 20:
        print("Окончание программы по обнаружению движущихся обьектов")
        end = datetime.now()
        elasped1 = (end - start1).total_seconds()
        break
        # check to see if the frame should be displayed to our screen
FPS1 = counter_fps1 / elasped1
# stop the timer and display FPS information
print("[INFO] elasped time:", elasped1)
print("[INFO] approx. FPS:", FPS1)
# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()


