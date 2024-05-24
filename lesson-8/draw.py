import os.path as path

import cv2

img = cv2.imread(path.join('.','white.jpeg'))

#line


print (img.shape)
cv2.line(img,(150,80),(300,168),(0,255,0),5)


#Rect

cv2.rectangle(img,(150,80),(300,168),(0,255,0),5)

#Circle

cv2.circle(img,(425,289),250,(0,255,0),5)

#text

font = cv2.FONT_HERSHEY_SIMPLEX

#El 200 afecta x y el otro y
cv2.putText(img,'OpenCV',(180,289), font, 4,(0,0,0),2)


cv2.imshow('img',img)
cv2.waitKey(0)

