import cv2
cap=cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
addres="http://192.168.43.1:8080/video"
cap.open(addres)
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break