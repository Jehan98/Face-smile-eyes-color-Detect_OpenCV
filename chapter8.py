import cv2
import numpy as np

img = cv2.imread("C:/Users/ASUS/Pictures/Camera Roll/shapes_ALL.jpg")
img = cv2.resize(img, (378, 227))
imgCopy = img.copy()
cv2.imshow("Shapes", img)
cv2.waitKey(0)

# FOR IMAGE CONCATENATION ______________________________________


def hconcat_resize(img_list, interpolation = cv2.INTER_CUBIC):
    # take minimum width
    w_min = min(img.shape[1] for img in img_list)
    # resizing images
    im_list_resize = [cv2.resize(img, (w_min, int(img.shape[0] * w_min / img.shape[1])), interpolation=interpolation) for img in img_list]
    # return final image
    return cv2.hconcat(im_list_resize)

# SHAPES ________________________________________________________


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 100)
imgConcat = hconcat_resize([imgGray, imgBlur, imgCanny])
cv2.imshow("images", imgConcat)
cv2.waitKey(0)


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            cv2.drawContours(imgCopy, contour, -1, (255, 0, 255), 2)
            perimeter = cv2.arcLength(contour, True)
            conors = cv2.approxPolyDP(contour, 0.02*perimeter, True)
            num_cornors = conors.shape[0]  # if 3 then triangle
            x, y, w, h = cv2.boundingRect(conors)
            cv2.rectangle(imgCopy, (x-5, y-5), (x+w+5, y+h+5), (0, 255, 0), 2)  # draw surrounding squares

            if num_cornors == 3:
                object_type = "Triangle"
            elif num_cornors == 4:
                aspRatio = float(w)/h
                if aspRatio < 1.3 and aspRatio > 0.7:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            else:
                object_type = "Circle"

            cv2.putText(imgCopy, object_type, ((x + w//2 - 10), (y + h//2 - 10)), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            print("Area = " + str(area) + " | Perimeter = " + str(perimeter) + " | Num of Corners = " + str(num_cornors) +
                  " | Object Type = " + object_type + " | width = " + str(w) + " | height = " + str(h))


getContours(imgCanny)
cv2.imshow("FINAL", imgCopy)
cv2.waitKey(0)

