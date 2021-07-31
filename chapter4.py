import cv2
import numpy as np

# SHAPES

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
img[10: 100, 10:100, 2] = 255
cv2.imshow("Image", img)
cv2.waitKey(0)

# LINES

cv2.line(img, (0, 0), (300, 300), (0, 200, 200), 3)
cv2.imshow("Image", img)
cv2.waitKey(0)

# RECTANGLE

cv2.rectangle(img, (300, 300), (400, 400), (0, 0, 255), 3)
cv2.imshow("Image", img)
cv2.waitKey(0)

# CIRCLE

cv2.circle(img, (400, 400), 100, (255, 255, 0), 2)
cv2.imshow("Image", img)
cv2.waitKey(0)

# TEXT

cv2.putText(img, "TEST OPENCV", (100, 300), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)
cv2.imshow("Image", img)
cv2.waitKey(0)
