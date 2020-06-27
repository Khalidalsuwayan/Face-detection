import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv.imread('faces_for_test.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces:
    cv.rectangle(img, pt1=(x, y), pt2=(x+w, y+h), color=(255, 0, 0), thickness=3)

cv.imshow('Image', img)
cv.waitKey(0)