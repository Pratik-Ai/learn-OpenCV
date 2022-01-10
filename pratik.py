import cv2

import numpy as np

def empty(a):
    pass

cap = cv2.VideoCapture(0)
cap.set(3,1280) # length code 3
cap.set(4,1040) # breadth code 4
cap.set(10,100)# brightness code 10

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("bru Min","TrackBars",0,179,empty)
cv2.createTrackbar("bru Max","TrackBars",19,179,empty)
cv2.createTrackbar("era Min","TrackBars",0,179,empty)
cv2.createTrackbar("era Max","TrackBars",19,179,empty)
while True:

    b_min = cv2.getTrackbarPos("bru Min","TrackBars")
    b_max = cv2.getTrackbarPos("bru Max", "TrackBars")
    e_min = cv2.getTrackbarPos("era Min", "TrackBars")
    e_max = cv2.getTrackbarPos("era Max", "TrackBars")

    print(b_min, b_max, e_min, e_max)

    lower = np.array([b_min, e_min])
    upper = np.array([b_min, e_min])
    # mask = cv2.inRange(img, lower, upper)
    # imgResult = cv2.bitwise_and(img, img, mask=mask)