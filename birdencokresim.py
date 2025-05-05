import cv2

path = "Resources/lena.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgA = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
imgBlur = cv2.GaussianBlur(img,(99,99),0)
cv2.imshow("lena",img)
cv2.imshow("graylena",imgGray)
cv2.imshow("Alena",imgA)
cv2.imshow("blurlena",imgBlur)

cv2.waitKey(0)
