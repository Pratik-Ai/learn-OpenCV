import cv2
cap = cv2.VideoCapture(0)
cap.set(3,1280)# length code 3
cap.set(4,1040)# breadth code 4
cap.set(10,100)# brightness code 10

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break