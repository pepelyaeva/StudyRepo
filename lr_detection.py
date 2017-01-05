import cv2

# Вывод на экран видеопотока.
cam = cv2.VideoCapture(0)
while cv2.waitKey(10) != 0x1b: # ESC
	_,frame = cam.read()
	cv2.imshow("features", frame)
