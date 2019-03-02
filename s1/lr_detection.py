import sys
import cv2,os
import numpy as np
from PIL import Image
import time

# Для детектирования лиц используем каскады Хаара.
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Для распознавания используем локальные бинарные шаблоны.
recognizer = cv2.face.createLBPHFaceRecognizer(1,8,8,8,123)

def get_images(path):
    # Ищем все фотографии и записываем их в image_paths
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.full.png')]
    
    images = []
    labels = []

    for image_path in image_paths:
        # Переводим изображение в черно-белый формат и приводим его к формату массива
        gray = Image.open(image_path).convert('L')
        image = np.array(gray, 'uint8')
        # Из каждого имени файла извлекаем номер человека, изображенного на фото
        subject_number = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        print(subject_number)
        # Определяем области где есть лица
        faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        print(faces)
        # Если лицо нашлось добавляем его в список images, а соответствующий ему номер в список labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(subject_number)
            # В окне показываем изображение
            cv2.imshow("", image[y: y + h, x: x + w])
            print(image_path)
            # cv2.waitKey(500)
    return images, labels

# Путь к фотографиям
path = './yalefaces'
# Получаем лица и соответствующие им номера
images, labels = get_images(path)
cv2.destroyAllWindows()

# Обучаем программу распознавать лица
recognizer.train(images, np.array(labels))

# Вывод на экран видеопотока.
cam = cv2.VideoCapture('Mult.mp4')
while cam.isOpened():
	_,frame = cam.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	image = np.array(gray, 'uint8')
	faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

	for (x, y, w, h) in faces:
		# Если лица найдены, пытаемся распознать их
		# Функция  recognizer.predict в случае успешного расознавания возвращает номер и параметр confidence,
		# этот параметр указывает на уверенность алгоритма, что это именно тот человек, чем он меньше, тем больше уверенность
		img = image[y: y + h, x: x + w]
		number_predicted, conf = recognizer.predict(img)
		cv2.imshow("Recognizing Face", img)

		if conf < 100:			
			print ("{} is Correctly Recognized with confidence {}".format(number_predicted, conf))			
		else:
			print ("{} is Incorrect Recognized {}".format(number_predicted, conf))
			if input("You want save this man? (y/n) ") == "y":
				name = input("Enter name: ")
				# time = time.asctime()
				idface=input("Enter id: ")
				cv2.imwrite(os.path.join(path, "subject{}.png".format(idface)) , img)
				cv2.imwrite(os.path.join(path, "subject{}.full.png".format(idface)), gray)
				images, labels = get_images(path)
				recognizer.train(images, np.array(labels))
		cv2.waitKey(1000)

cam.release()
