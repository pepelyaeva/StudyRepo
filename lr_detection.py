import sys
import cv2
import numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(img):
	# Переводим изображение в черно-белый формат
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# Определяем области где есть лица.
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	for (x, y, w, h) in faces:
		# Если лицо нашлось, прорисовываем синий прямоугольник.
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		# Определяем области где есть глаза.
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			# Если глаз нашелся, прорисовываем зеленый прямоугольник.
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)    
	return img

# Вывод на экран видеопотока.
cam = cv2.VideoCapture(0)
while cv2.waitKey(10) != 0x1b:
     _,frame =cam.read()
     frame = numpy.asarray(detect(frame))
     # В окне показываем изображение.
     cv2.imshow("features", frame)