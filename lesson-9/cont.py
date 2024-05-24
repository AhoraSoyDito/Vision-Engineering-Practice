import os.path as path
import cv2 


img = cv2.imread(path.join('.','lesson-9.jpg'))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#!--- SOLO ACEPTA IMAGENES DE UN SOLO CANAL

#for cnt in contours:
#    print (cv2.contourArea(cnt))
#* esto se hace para poder eliminar el ruido que hay en la imagen

for cnt in contours:
    if cv2.contourArea(cnt) > 95:
        #cv2.drawContours(img,[cnt],-1,(0,255,0),2)
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)




cv2.imshow('image',img)
# cv2.imshow('thresh',thresh)
# cv2.imshow('contours',contours)
cv2.waitKey(0)
cv2.destroyAllWindows()