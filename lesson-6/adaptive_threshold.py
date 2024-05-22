import os.path as path
import cv2

img = cv2.imread(path.join('.','poema.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

#!--- Este ultimo tien que ser Odd

cv2.imshow("resultado", thresh)
cv2.imshow("original", img_gray)

cv2.waitKey(0)
