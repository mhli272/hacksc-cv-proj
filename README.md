# hacksc-cv-proj
This program uses the concept of computer stereo vision to calculate the 3D position of people in a pair of images taken by two cameras a small distance apart simulataneously. 

Parameters such as the pixel length, height of the picture, the distance that the cameras are seperated by, the one-half of the left-right angle view of the camera, and one-hlf of the up--down angle view of the camera are needed.

calcDist.py is the helper file that does the math ad calculates 3D coordinates based off of pixel coordinates in the two pictures and the parameters given above.

face_detection.py is the helper file that detects people's faces in a picture and returns a list of the pixel coords for the faces.

tester.py is the main file that combines everything. It has a very simple CLI based UI. But if you want to test different image files, you have to drag them into this folder and specify the name by changin two variables in tester.py