import cv2
import numpy as np

img = cv2.imread("C:/Users/ASUS/Pictures/Camera Roll/Lambo.jpg")
imgResize = cv2.resize(img, (512, 288))

# HSV

imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
imgHor = np.hstack((imgResize, imgHSV))
cv2.imshow("HSV", imgHor)

# TRACKBARS

def empty(a):
    pass

cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars", 640, 340)
cv2.createTrackbar("Hue Min", "Track Bars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Track Bars", 71, 255, empty)
cv2.createTrackbar("Sat Max", "Track Bars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Track Bars", 40, 255, empty)
cv2.createTrackbar("Val Max", "Track Bars", 255, 255, empty)

while True:
    imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max", "Track Bars")
    s_min = cv2.getTrackbarPos("Sat Min", "Track Bars")
    s_max = cv2.getTrackbarPos("Sat Max", "Track Bars")
    v_min = cv2.getTrackbarPos("Val Min", "Track Bars")
    v_max = cv2.getTrackbarPos("Val Max", "Track Bars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    imgFinal = cv2.bitwise_and(imgResize, imgResize, mask=mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Final", imgFinal)

    if cv2.waitKey(1) == ord("q"):
        break