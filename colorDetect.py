import cv2
import numpy as np

# VIDEO HANDLING

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 1000)

Colors = [[143, 46, 0, 255, 255, 255]]  # colors are set to detect purple rose


def findColor(img, color):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(color[0][0:3])
    upper = np.array(color[0][3:6])
    imgMask = cv2.inRange(imgHSV, lower, upper)

    imgFinal = cv2.bitwise_and(img, img, mask=imgMask)

    return imgMask, imgFinal


while True:
    success, img = cap.read()
    imgMask, imgFinal = findColor(img, Colors)
    cv2.imshow("Mask", imgMask)
    imgHor = np.hstack((img, imgFinal))
    cv2.imshow("Color Detect", imgHor)

    if cv2.waitKey(1) == ord("q"):
        break
