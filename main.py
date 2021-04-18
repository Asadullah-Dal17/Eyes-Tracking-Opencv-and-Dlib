import cv2 as cv
import numpy as np
import module as m


cameraID = 0

# creating camera object
camera = cv.VideoCapture(cameraID)

while True:
    # getting frame from camera
    ret, frame = camera.read()

    # converting frame into Gry image.
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # calling the face detector funciton
    image, face = m.faceDetector(frame, grayFrame)

    # calling landmarks detector funciton.
    image, PointList = m.faceLandmakDetector(frame, grayFrame, face, False)
    print(PointList)

    # showing the frame on the screen
    cv.imshow('Frame', image)

    # defining the key to Quite the Loop
    key = cv.waitKey(1)

    # if q is pressed on keyboard: quit
    if key == ord('q'):
        break
# closing the camera
camera.release()
# closing  all the windows
cv.destroyAllWindows()
