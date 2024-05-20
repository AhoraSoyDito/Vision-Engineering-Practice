import cv2 

#Ahora con Webcam
webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if ret:
        cv2.imshow("frame",frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break#salen de los fps a los que esta el video, si son 25FPS entonces es un frame cada 0.04s

webcam.release()
cv2.destroyAllWindows()