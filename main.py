import cv2 as cv
import numpy as np
import module as m

# Variables
COUNTER = 0
TOTAL_BLINKS = 0
CLOSED_EYES_FRAME = 3
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
    # print(PointList)

    RightEyePoint = PointList[36:42]
    LeftEyePoint = PointList[42:48]
    leftRatio, topMid, bottomMid = m.blinkDetector(LeftEyePoint)
    rightRatio, rTop, rBottom = m.blinkDetector(RightEyePoint)
    cv.circle(image, topMid, 2, m.YELLOW, -1)
    cv.circle(image, bottomMid, 2, m.YELLOW, -1)

    blinkRatio = (leftRatio + rightRatio)/2

    if blinkRatio > 4:
        COUNTER += 1
        cv.putText(image, f'Blink', (50, 50), m.fonts, 1, m.LIGHT_BLUE, 2)
        # print("blink")
    else:
        if COUNTER > CLOSED_EYES_FRAME:
            TOTAL_BLINKS += 1
            COUNTER = 0
    cv.putText(image, f'{TOTAL_BLINKS}', (50, 80),
               m.fonts, 1.2, m.LIGHT_BLUE, 2)

    # for p in LeftEyePoint:
    #     cv.circle(image, p, 3, m.MAGENTA, 1)

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
