import math
#Calculates the 3D position of the object to the camera
#outputs:
#   dx is the left right distance of the object to the centerline of the cameras
#   dy is the front back distance from the object to the cameras
#   dz is tje up down distance from the object to the cameras
#inputs:
#    coords1(x1, y1) is the pixel coord of the object with the left camera
#    coords2(x2, y2) is the pixel coord of the object with the right camera
#    camDist is the distance between the two cameras
#    picLength is the legnth of the picture in pixels
#    picHeight is the height of the picture in pixels
#    LRangle is half of the left-right view angle of the camera
#    UDangle is half of the up-down view angle of the camera
def positionToCam(coords1, coords2, camDist, picLength, picHeight, LRangle, UDangle):
    x1, y1 = coords1
    x2, y2 = coords2
    a = (x1-x2)/picLength
    #the y distance from object to camera
    dy = (1/a)*camDist/(2*math.tan(LRangle*math.pi/180))
    #the left-right distance from object to the middle of the camera
    dx = (((x1 + x2)/picLength)- 0.5)*dy*math.tan(LRangle*math.pi/180)
    #the vertical distance the object is from the camera
    dz = (1-((y1+y2)/(2*picHeight))-0.5)*2*dy*math.tan(UDangle*math.pi/180)
    return dx, dy, dz


#calculates the distance between two 3D coords with 6 doubles as input
def calcDistance(coords1, coords2):
    sum = 0
    for a in coords1:
        for b in coords2:
            sum += math.pow(a-b, 2)
    return math.sqrt(sum)



#s is a dictionary with 2d pixel coords (double tuple) as keys and 3d coords (double tuple) as value
#dis is the minimum distance that we want the people to be apart
#we should choose 
def checkAll(s, dis):
    ans = {}
    temp = s
    for i in s:
        temp -= i
        for j in temp:
            if(calcDistance(s[i], s[j]) <= dis):
                ans += j
                ans += i
    return ans

#testing
print(positionToCam((150, 300), (148, 300), 2, 200, 400, 30, 30))

