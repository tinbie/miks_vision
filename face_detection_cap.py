#python2.7 utf8

import numpy
import cv2
from time import sleep

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    sleep(1)

    while True:
        frame = cap.read()[1]
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_detect = cv2.CascadeClassifier('haarcascade_frontalface.xml')
        faces = face_detect.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(gray_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('face-detection', gray_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows
