import cv2
import numpy as np

img = cv2.imread("C:/Users/ASUS/Pictures/Camera Roll/harry-potter-5.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)

# WRAP PERSPECTIVE

width, height = 300, 300
pts1 = np.array([[950, 1172], [636, 1344], [1484, 1185], [1480, 1368]], np.float32) # dtype should be float32
print(pts1)
pts2 = np.array([[0, 0], [0, height], [width, 0], [width, height]], np.float32)
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOut = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Warp", imgOut)
cv2.waitKey(0)