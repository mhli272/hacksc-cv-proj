import cv2
import numpy as np
import imutils
import calcDist
import face_detection

def main():
    image = "pic1.jpg"
    image2 = "pic2.jpg"
    photoOneCoords = face_detection.face_detect(image)
    photoTwoCoords = face_detection.face_detect(image2)

    print(photoOneCoords)
    print(photoTwoCoords)

    camDist = 1
    picLength = 1
    picHeight = 1
    LRangle = 60
    UDangle = 60

    combinedCoords = []

    for i in range(len(photoOneCoords)):
        combinedCoords.append(calcDist.positionToCam(photoOneCoords[i], photoTwoCoords[i], camDist, picLength, picHeight, LRangle, UDangle))

    distance = 6

    dict = {}
    for i in range(len(photoOneCoords)):
        dict[photoOneCoords[i]] = combinedCoords[i]
    notDistanced = calcDist.checkAll(dict, distance)

    print("not Distanced:")
    print(notDistanced)



main()