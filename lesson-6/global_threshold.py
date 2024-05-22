import cv2
import numpy as np
import os.path as path

img = cv2.imread(path.join('..','data','bird.jpeg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 90, 255, cv2.THRESH_BINARY)

cv2.imshow('image',img)

#!--- Mostrando Dif
cv2.imshow('Thresh', thresh)

cv2.imshow('img_gray', img_gray)


cv2.waitKey(0)

