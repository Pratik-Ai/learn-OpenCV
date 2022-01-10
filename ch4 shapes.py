import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
# for color
# img[:]=0,0,255

# for making line
# cv2.line(img,(0,0),(300,300),(0,255,0),(3))
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),(3))

cv2.rectangle(img,(0,0),(250,350),(0,0,230),3)
cv2.circle(img,(400,50),50,(255,255,0),5)
cv2.putText(img,"OpenCv",(300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),2)
cv2.imshow("image",img)

cv2.waitKey(0)