import cv2
import numpy as np
import imutils

protopath = "deploy.prototxt"
modelpath = "res10_300x300_ssd_iter_140000.caffemodel"
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

#takes in filename, and runs face detection on the file
#makes a picture in the directory called Result.jpg with the result
#outputs the coords for all the faces as well
def face_detect(filename):
    image = cv2.imread(filename)
    image = imutils.resize(image, width=600)
    (H, W) = image.shape[:2]
    face_blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), False, False)
    detector.setInput(face_blob)
    face_detections = detector.forward()

    photoCoords = []
    
    #detecting the faces of the first picture
    for i in np.arange(0, face_detections.shape[2]):
        confidence = face_detections[0, 0, i, 2]
        if confidence > 0.5:

            face_box = face_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = face_box.astype("int")
            centerX = int(startX + ((endX - startX) / 2))
            centerY = int(startY + ((endY - startY) / 2))
            cv2.circle(image, (centerX, centerY), 5, (0,0,255), 2)
            photoCoords.append((centerX,centerY))


    cv2.imshow("Result.jpg", image)
    cv2.imwrite("Result.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return photoCoords

def draw_Rect(filename):
    image = cv2.imread(filename)
    image = imutils.resize(image, width=600)
    (H, W) = image.shape[:2]
    face_blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), False, False)
    detector.setInput(face_blob)
    face_detections = detector.forward()
    for i in np.arange(0, face_detections.shape[2]):
        confidence = face_detections[0, 0, i, 2]
        if confidence > 0.5:
            face_box = face_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = face_box.astype("int")
            cv2.rectangle(image, (startX, startY), (endX, endY), (0,0,255), 4)

    cv2.imwrite("Result.jpg", image)
    cv2.imshow("Result.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
