import cv2
import numpy as np
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgcanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgcanny, kernel, iterations=1)
imgerode = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("gray image",imgGray)
cv2.imshow("blur image",imgBlur)
cv2.imshow("canny image",imgcanny)
cv2.imshow("dialate",imgDialation)
cv2.imshow("erode",imgerode)
cv2.waitKey(0)