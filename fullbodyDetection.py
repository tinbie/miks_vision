#python2.7 utf8

import sys
import cv2

img = cv2.imread(sys.argv[1])
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fullbodies_detect = cv2.CascadeClassifier('haarcascade_fullbody.xml')
bodies = fullbodies_detect.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))

print "Found {0} bodies!".format(len(bodies))

for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("detected bodies", img)
cv2.waitKey(0)