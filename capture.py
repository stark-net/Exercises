from cv2 import *
from cv2 import VideoCapture,imshow,imwrite,waitKey,destroyWindow
cam = VideoCapture(0)
result, image = cam.read()
if result:
	imshow("GeeksForGeeks", image)
	imwrite("GeeksForGeeks.png", image)
	waitKey(0)
	destroyWindow("GeeksForGeeks")
else:
	print("No image detected. Please! try again")

