import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)


path = "Resources/lena.png"
img = cv2.imread(path)
img = cv2.resize(img,(400,600))

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgA = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
imgBlur = cv2.GaussianBlur(img,(99,99),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)





cv2.imshow("lena",img)
cv2.imshow("graylena",imgGray)
cv2.imshow("Alena",imgA)
cv2.imshow("blurlena",imgBlur)
cv2.imshow("cannyLena",imgCanny)
cv2.imshow("dilatedLena", imgDilation)
cv2.imshow("erodedLena", imgEroded)

cv2.waitKey(0)
