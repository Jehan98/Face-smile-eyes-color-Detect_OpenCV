import cv2

# PHOTO HANDLING

img = cv2.imread("C:/Users/ASUS/Pictures/Camera Roll/Jehan.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)

# VIDEO HANDLING

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 1000)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) == ord("q"):
        break




