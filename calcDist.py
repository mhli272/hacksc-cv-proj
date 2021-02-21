import math
#Calculates the 3D position of the object to the camera
#dx is left right
#dy is front back
#dz is up down
#x1, y1 is left camera; x2, y2 is right camera
def positionToCam(x1, y1, x2, y2, camDist, picLength, picHeight, LRangle, UDangle):
    a = (x1-x2)/picLength
    #the y distance from object to camera
    dy = (1/a)*camDist/(2*math.tan(LRangle*math.pi/180))
    #the left-right distance from object to the middle of the camera
    dx = (((x1 + x2)/picLength)- 0.5)*dy*math.tan(LRangle*math.pi/180)
    #the verticle distance the object is from the camera
    dz = (1-((y1+y2)/(2*picHeight))-0.5)*2*dy*math.tan(UDangle*math.pi/180)
    return (dx, dy, dz)

#testing
print(positionToCam(150, 300, 148, 300, 2, 200, 400, 30, 30))

