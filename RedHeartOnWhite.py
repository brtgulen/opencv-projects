import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8)
print(img)
img [:] = 255,255,255
cv2.line(img,(300,450),(150,250),(0,0,255),25)
cv2.line(img,(300,450),(450,250),(0,0,255),25)
cv2.line(img,(150,250),(225,150),(0,0,255),25)
cv2.line(img,(225,150),(300,250),(0,0,255),25)
cv2.line(img,(300,250),(375,150),(0,0,255),25)
cv2.line(img,(375,150),(450,250),(0,0,255),25)




cv2.imshow("image",img)
cv2.waitKey(0)