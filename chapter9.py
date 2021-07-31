import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/gameofthrones.jpg")
img = cv2.resize(img, (766, 454))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.01, 15, minSize=(100, 100))

for face in faces:
    x, y, w, h = face
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

imgCopy = img.copy()
cv2.imshow("Shapes", img)
cv2.waitKey(0)