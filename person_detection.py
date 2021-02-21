import cv2
import numpy as np
import imutils
import calcDist

protopath = "MobileNetSSD_deploy.prototxt"
modelpath = "MobileNetSSD_deploy.caffemodel"
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)
detector2 = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chari", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

def main():

#distance between pictures is 0.127 meters

    image = cv2.imread("IMG_0049.jpg")
    image = imutils.resize(image, width=600)
    image2 = cv2.imread("people_line.jpg")
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

    cv2.imwrite("Results1.jpg", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite("Results2.jpg", image2)




main()