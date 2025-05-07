import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8)
print(img)
img [:] = 0,255,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,255,255),100)
cv2.rectangle(img,(400,100),(500,200),(0,0,255),cv2.FILLED)
cv2.circle(img,(150,450),100,(255,0,0),cv2.FILLED)
cv2.circle(img,(450,150),50,(0,255,0),cv2.FILLED)
cv2.putText(img,"Draw Shapes",(200,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,0),3)



cv2.imshow("image",img)
cv2.waitKey(0)