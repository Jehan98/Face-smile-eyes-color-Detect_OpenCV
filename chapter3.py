# RESIZE IMAGE
import cv2
import numpy as np

img = cv2.imread("C:/Users/ASUS/Pictures/Camera Roll/Jehan.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.imshow("Resized Image", imgResize)
cv2.waitKey(0)

# CROP IMAGE
imgCropped = img[0:720, 500:700]
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)