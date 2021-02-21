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
    #the vertical distance the object is from the camera
    dz = (1-((y1+y2)/(2*picHeight))-0.5)*2*dy*math.tan(UDangle*math.pi/180)
    return dx, dy, dz

#calculates the distance between two 3D coords
def calcDistance(x1, y1, z1, x2, y2, z2):
    a = math.pow(x1-x2, 2)
    b = math.pow(y1-y2, 2)
    c = math.pow(z1-z2, 2)
    return math.sqrt(a+b+c)

#s is a dictionary with 2d pixel coords (double tuple) as keys and 3d coords (double tuple) as value
def checkAll(s, dis):
    ans = {}
    temp = s;
    for i in s:
        temp -= i
        for j in temp:
            x1 = i[0]
            y1 = i[1]
            z1 = i[2]
            x2 = j[0]
            y2 = j[1]
            z2 = j[2]
            if(calcDistance(x1, y1, z1, x2, y2, z2) <= dis):
                ans += j
                ans += i


#testing
print(positionToCam(150, 300, 148, 300, 2, 200, 400, 30, 30))

