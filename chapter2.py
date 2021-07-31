# GREY SCALE/ BLUR- IMG PROCESSING
import cv2
import numpy as np

img = cv2.imread("C:/Users/ASUS/Pictures/Camera Roll/Jehan.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)  # edge detection
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) # increased thickness
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) # decreased thickness

cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)
cv2.imshow("Dilation Image", imgDialation)
cv2.waitKey(0)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)