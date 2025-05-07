import cv2

path = 'Resources/yol.png'
img = cv2.imread(path)
print(img.shape)
cv2.imshow("road", img)

width = 400
height = 400

imgResized = cv2.resize(img,(width,height))
print(imgResized.shape)
cv2.imshow("Resized road",imgResized)
"""
FOR GRAY IMAGE
imgGray = cv2.cvtColor(imgResized,cv2.COLOR_BGR2GRAY)
print(imgGray.shape)
cv2.imshow("Gray Road",imgGray)
"""
"""
OR
"""
imgGray = cv2.imread(path,0)
print(imgGray.shape)
cv2.imshow("Gray Road", imgGray)

imgCropped = img[240:501,0:953]
cv2.imshow("cropped road",imgCropped)
imgCropped2 = img[0:501,430:490]
cv2.imshow("Cropped road 2",imgCropped2)

imgCroppedResize = cv2.resize(imgCropped,(imgGray.shape[1],imgGray.shape[0]))
cv2.imshow("img Cropped resized",imgCroppedResize)

imgCroppedResize2 = cv2.resize(imgCropped2,(img.shape[1],img.shape[0]))
cv2.imshow("img cropped resized 2",imgCroppedResize2)



cv2.waitKey(0)
