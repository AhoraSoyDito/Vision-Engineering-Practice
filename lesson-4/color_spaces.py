import cv2
import os
import numpy as np

img = cv2.imread(os.path.join('..','data','bird.jpeg'))

imgrbg=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Aqui estoy cambiando la posicion  de los colores rojo y azul
cv2.imwrite(os.path.join('..','data','bird_bgr.jpeg'),imgrbg)

imggray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(os.path.join('..','data','bird_gray.jpeg'),imggray)

#!----ESTE ES BASTANTE UTIL
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite(os.path.join('..','data','bird_hsv.jpeg'),img_hsv)
cv2.imshow("HSV", img_hsv)
#!----

cv2.imshow("BGR", img)    
cv2.imshow("RGB", imgrbg)
cv2.imshow("GRAY",imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()

