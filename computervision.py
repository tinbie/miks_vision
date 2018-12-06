#python2.7 utf8

import numpy
import cv2
from time import sleep

def getStartImage():
    return img

def getImage():
    return img

def getCoordinates():
    pass

def drawRect(img, left_upper_corner, right_bottom_corner):
    return img

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    sleep(2)
    startImg = getStartImage()
    sleep(1)

    try:
        while True:
            frame = cap.read()[1]
            actualImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # subtract actual img from starting img
            diffImg = startImg - actualImg
            


    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows
