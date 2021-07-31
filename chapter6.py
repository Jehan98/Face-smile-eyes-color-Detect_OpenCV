import cv2
import numpy as np

img = cv2.imread("C:/Users/ASUS/Pictures/Camera Roll/Jehan1.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)

# JOINING IMAGES

imgHor = np.hstack((img, img))
cv2.imshow("Output1", imgHor)
cv2.waitKey(0)
imgVer = np.vstack((img, img))
cv2.imshow("Output2", imgVer)
cv2.waitKey(0)