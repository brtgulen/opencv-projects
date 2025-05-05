import cv2

path = "Resources/lena.png"


img = cv2.imread(path,0)

cv2.imshow("lena",img)
cv2.waitKey(0)
