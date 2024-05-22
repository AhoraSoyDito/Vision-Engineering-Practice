import os.path as path
import numpy as np
import cv2

jugadores = cv2.imread(path.join('.', 'jugadores.jpg'))

jugadores_gray = cv2.cvtColor(jugadores, cv2.COLOR_BGR2GRAY) 

cv2.imshow("jugadores", jugadores)  

#!---------
ret, thresh1 = cv2.threshold(jugadores_gray, 70, 255, cv2.THRESH_BINARY)
k_size = 3
thresh_blur = cv2.medianBlur(thresh1,(k_size))
ret, thresh2 = cv2.threshold(thresh_blur, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('1',thresh1)
cv2.imshow('2',thresh2)
#!---------

tresh_a = cv2.adaptiveThreshold(jugadores_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow('adaptive',tresh_a)

cv2.waitKey(0)
cv2.destroyAllWindows()