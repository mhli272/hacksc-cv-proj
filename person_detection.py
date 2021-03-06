import cv2
import numpy as np
import imutils
import calcDist

protopath = "MobileNetSSD_deploy.prototxt"
modelpath = "MobileNetSSD_deploy.caffemodel"
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)
detector2 = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle",
 "bus", "car", "cat", "chari", "cow", "diningtable", "dog", "horse", "motorbike", "person",
  "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

def main():

    left_file = "pic1.jpg"
    right_file = "pic2.jpg"



    image = cv2.imread(left_file)
    image = imutils.resize(image, width=600)
    image2 = cv2.imread(right_file)
    image2 = imutils.resize(image2, width=600)
    (H, W) = image.shape[:2]
    (H2, W2) = image2.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)
    blob2 = cv2.dnn.blobFromImage(image2, 0.007843, (W2, H2), 127.5)

    detector.setInput(blob)
    person_detections = detector.forward()

    photoOneCoords = []
    photoTwoCoords = []

    #detecting the people of the first picture
    for i in np.arange(0, person_detections.shape[2]):
        confidence = person_detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(person_detections[0, 0, i, 1])

            if CLASSES[idx] != "person":
                continue

            person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = person_box.astype("int")
            centerX = int(startX + ((endX - startX) / 2))
            centerY = int(startY + ((endY - startY) / 2))
            cv2.circle(image, (centerX, centerY), 5, (0,0,255), 2)
            photoOneCoords.append((centerX,centerY))

    print(photoOneCoords)

    detector2.setInput(blob2)
    person2_detections = detector2.forward()

    # detecting the people of the second picture
    for i in np.arange(0, person2_detections.shape[2]):
        confidence = person2_detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(person2_detections[0, 0, i, 1])

            if CLASSES[idx] != "person":
                continue

            person2_box = person2_detections[0, 0, i, 3:7] * np.array([W2, H2, W2, H2])
            (startX, startY, endX, endY) = person2_box.astype("int")
            centerX = int(startX + ((endX - startX) / 2))
            centerY = int(startY + ((endY - startY) / 2))
            cv2.circle(image2, (centerX, centerY), 5, (0, 0, 255), 2)
            photoTwoCoords.append((centerX, centerY))

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

    cv2.imshow("Results", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("Results", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()