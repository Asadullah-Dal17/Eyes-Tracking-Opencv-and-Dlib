import cv2 as cv
import numpy as np
import dlib
import math

# variables
fonts = cv.FONT_HERSHEY_COMPLEX

# colors
YELLOW = (0, 247, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 242)
GOLDEN = (32, 218, 165)
LIGHT_BLUE = (255, 9, 2)
PURPLE = (128, 0, 128)
CHOCOLATE = (30, 105, 210)
PINK = (147, 20, 255)
ORANGE = (0, 69, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 255, 13)
LIGHT_CYAN = (255, 204, 0)
BLUE = (255, 0, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_RED = (2, 53, 255)


# face detector object
detectFace = dlib.get_frontal_face_detector()
# landmarks detector
predictor = dlib.shape_predictor(
    "Predictor/shape_predictor_68_face_landmarks.dat")

# function


def midpoint(pts1, pts2):
    x, y = pts1
    x1, y1 = pts2
    xOut = int((x + x1)/2)
    yOut = int((y1 + y)/2)
    # print(xOut, x, x1)
    return (xOut, yOut)


def eucaldainDistance(pts1, pts2):
    x, y = pts1
    x1, y1 = pts2
    eucaldainDist = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

    return eucaldainDist

# creating face detector function


def faceDetector(image, gray, Draw=True):
    cordFace1 = (0, 0)
    cordFace2 = (0, 0)
    # getting faces from face detector
    faces = detectFace(gray)

    face = None
    # looping through All the face detected.
    for face in faces:
        # getting coordinates of face.
        cordFace1 = (face.left(), face.top())
        cordFace2 = (face.right(), face.bottom())

        # draw rectangle if draw is True.
        if Draw == True:
            cv.rectangle(image, cordFace1, cordFace2, GREEN, 2)
    return image, face


def faceLandmakDetector(image, gray, face, Draw=True):
    # calling the landmarks predictor
    landmarks = predictor(gray, face)
    pointList = []
    # looping through each landmark
    for n in range(0, 68):
        point = (landmarks.part(n).x, landmarks.part(n).y)
        # getting x and y coordinates of each mark and adding into list.
        pointList.append(point)
        # draw if draw is True.
        if Draw == True:
            # draw circle on each landmark
            cv.circle(image, point, 3, ORANGE, 1)
    return image, pointList

# Blink detector function.


def blinkDetector(eyePoints):
    top = eyePoints[1:3]
    bottom = eyePoints[4:6]
    # finding the mid point of above points
    topMid = midpoint(top[0], top[1])
    bottomMid = midpoint(bottom[0], bottom[1])
    # getting the actual width and height eyes using eucaldainDistance function
    VerticalDistance = eucaldainDistance(topMid, bottomMid)
    HorizontalDistance = eucaldainDistance(eyePoints[0], eyePoints[3])
    # print()

    blinkRatio = (HorizontalDistance/VerticalDistance)
    return blinkRatio, topMid, bottomMid
