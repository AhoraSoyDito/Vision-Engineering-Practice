import os
import cv2

img = cv2.imread(os.path.join('.','data','bird.jpeg'))

print(img.shape) 
#(708,1000,3)

#primero es la with y despues la height
img_resized = cv2.resize(img, (500,354))
#esta es una cuarta parte de la imagen original

print(img_resized.shape)
#((480,640,3),(960,1280,3))
cv2.imwrite(os.path.join('.','data','bird_resized.jpeg'),img)

cv2.imshow('pic', img)
cv2.imshow('pic_resized', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

