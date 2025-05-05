import cv2


frameWidth = 1400
frameHeight = 1500


cap = cv2.VideoCapture("Resources/fifa19.mp4")

while True:
    success,img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord("a"):
        break