import cv2
import numpy as np
import imutils
import calcDist
import face_detection

def main():
    image = "testing-pictures/far_left1.jpg"
    image2 = "testing-pictures/far_right1.jpg"
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
        face_detection.draw_Rect(image, photoOneCoords)
    else:
        print("Distanced!")



main()