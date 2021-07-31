import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier('Resources/haarcascade_smile.xml')
eyeCascade = cv2.CascadeClassifier("Resources/haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 1000)


def detectFaces(img):
    faces = faceCascade.detectMultiScale(img, 1.02, 10, minSize=(50, 50))
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


def detectSmile(img, img_face, x, y, w, h):
    smiles = smileCascade.detectMultiScale(img_face, 1.6, 5)
    for smile in smiles:
        x_face, y_face, w_face, h_face = smile
        if (y + y_face + h_face) > (y + h * 3 / 4) and (w_face*h_face)/(w*h) > 0.1:        # assuming mouth is in the lower part of the face
            cv2.rectangle(img, (x+x_face, y+y_face), (x+x_face + w_face, y+y_face + h_face), (255, 0, 255), 2)


def detectEyes(img, img_face, x, y, w, h):
    eyes = eyeCascade.detectMultiScale(img_face, 1.1, 3)
    for eye in eyes:
        x_eye, y_eye, w_eye, h_eye = eye
        cv2.circle(img, (x + x_eye + w_eye//2, y + y_eye + h_eye//2), (w_eye + h_eye)//4, (255, 0, 0), 2)


while True:
    max_face_area = 0
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.01, 10, minSize=(50, 50))   # detecting faces using cascade
    for face in faces:
        x, y, w, h = face
        face_area = w*h
        if max_face_area < face_area:           # to limit the wrong detecting faces which by adding an area limit
            max_face_area = face_area
        if face_area/max_face_area > 0.5:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            imgFace = imgGray[y:y+h, x:x+w]                    # crop the detected faces
            detectSmile(img, imgFace, x, y, w, h)              # only to detect smiles inside faces
            detectEyes(img, imgFace, x, y, w, h)

    cv2.imshow("Smile", img)

    if cv2.waitKey(1) == ord("q"):
        break
