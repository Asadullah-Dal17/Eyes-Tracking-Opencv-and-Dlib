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
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
Recoder = cv.VideoWriter('output.mp4', fourcc, 15.0, (640, 480))

while True:
    # getting frame from camera
    ret, frame = camera.read()

    # converting frame into Gry image.
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # calling the face detector funciton
    image, face = m.faceDetector(frame, grayFrame)
    if face is not None:

        # calling landmarks detector funciton.
        image, PointList = m.faceLandmakDetector(frame, grayFrame, face, False)
        # print(PointList)

        RightEyePoint = PointList[36:42]
        LeftEyePoint = PointList[42:48]
        leftRatio, topMid, bottomMid = m.blinkDetector(LeftEyePoint)
        rightRatio, rTop, rBottom = m.blinkDetector(RightEyePoint)
        # cv.circle(image, topMid, 2, m.YELLOW, -1)
        # cv.circle(image, bottomMid, 2, m.YELLOW, -1)

        blinkRatio = (leftRatio + rightRatio)/2
        cv.circle(image, (40, 40), (int(blinkRatio*4.3)), m.CHOCOLATE, -1)
        cv.circle(image, (40, 40), (int(blinkRatio*3.2)), m.CYAN, 2)
        cv.circle(image, (40, 40), (int(blinkRatio*2)), m.GREEN, 3)

        if blinkRatio > 4:
            COUNTER += 1
            cv.putText(image, f'Blink', (70, 50),
                       m.fonts, 0.8, m.LIGHT_BLUE, 2)
            # print("blink")
        else:
            if COUNTER > CLOSED_EYES_FRAME:
                TOTAL_BLINKS += 1
                COUNTER = 0
        cv.putText(image, f'Total Blinks: {TOTAL_BLINKS}', (430, 60),
                   m.fonts, 0.7, m.ORANGE, 2)

        # for p in LeftEyePoint:
        #     cv.circle(image, p, 3, m.MAGENTA, 1)
        mask, pos, color = m.EyeTracking(frame, grayFrame, RightEyePoint)

        # draw background as line where we put text.
        cv.line(image, (30, 90), (100, 90), color[0], 30)

        # writing text on above line
        cv.putText(image, f'{pos}', (35, 95), m.fonts, 0.6, color[1], 2)

        # showing the frame on the screen
        cv.imshow('Frame', image)
    else:
        cv.imshow('Frame', frame)

    Recoder.write(frame)

    # defining the key to Quite the Loop
    key = cv.waitKey(1)

    # if q is pressed on keyboard: quit
    if key == ord('q'):
        break
# closing the camera
camera.release()
# closing  all the windows
cv.destroyAllWindows()
