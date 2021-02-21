import cv2
import numpy as np
import imutils
import calcDist
import face_detection

def main():
    image = "testing-pictures/close_left.jpg"
    image2 = "testing-pictures/close_right.jpg"
    photoOneCoords = face_detection.face_detect(image)
    photoTwoCoords = face_detection.face_detect(image2)


    camDist = 0.127
    picLength = 600
    picHeight = 1134
    LRangle = 30.26
    UDangle = 30.47

    combinedCoords = []
    photoOneCoords.sort()
    photoTwoCoords.sort()
    print(photoOneCoords)
    print(photoTwoCoords)


    for i in range(len(photoOneCoords)):
        combinedCoords.append(calcDist.positionToCam(photoOneCoords[i], photoTwoCoords[i], camDist, picLength, picHeight, LRangle, UDangle))

    distance = 6
    print(combinedCoords)

    dict = {}
    for i in range(len(photoOneCoords)):
        dict[photoOneCoords[i]] = combinedCoords[i]
    notDistanced = calcDist.checkAll(dict, distance)

    if(len(notDistanced) != 0):
        print("not Distanced:")
    else:
        print("Distanced!")
    print(notDistanced)



main()