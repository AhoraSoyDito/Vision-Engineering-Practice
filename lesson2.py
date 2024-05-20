import os
import cv2
#leer imagen
image_path = os.path.join('.','data','bird.jpeg')
img = cv2.imread(image_path)
#Ver Video Video
#? Video_path = os.path.join(location)
#? cv2.VideoCapture(vieo_path)
#Escribir image
cv2.imwrite(os.path.join('.','data','bird_out.jpeg'),img)

# Ver imagen
cv2.imshow('image',img)
cv2.waitKey(0) #Lo que hace es esperar a que precione una keyboard (cantidad de milisegundos)
cv2.destroyAllWindows()
#Ver Video 
#? ret = True
#? while ret:
#?     ret, frame = video.read()
#!pa cuando se nos acaben los frames ret sigue siendo True 
    #? if ret: 
        #? cv2.imshow("image",frame)
        #? cv2.waitKey(40) #salen de los fps a los que esta el video, si son 25FPS entonces es un frame cada 0.04s
#? video.release()

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