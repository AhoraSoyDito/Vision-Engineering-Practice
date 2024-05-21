import cv2
import numpy as np
import os

img = cv2.imread(os.path.join("..", "data","bird.jpeg"))

#!----Define la proximidad del average que se esta haciendo
#!----mientras mas grande mas fuerte
k_size = 11
imgBlur = cv2.blur(img,(k_size, k_size))
cv2.imwrite(os.path.join("..","data","bird_blur.jpeg"), imgBlur)

#!-- Esto se utiliza para el ruido de la imagen

imgGausssianBlur = cv2.GaussianBlur(img, (k_size, k_size), 5)
cv2.imwrite(os.path.join('..','data','bird_gausian_blur.jpeg'),imgGausssianBlur)


img_median_blur = cv2.medianBlur(img,(k_size))
cv2.imwrite(os.path.join('..','data','bird_median_blur.jpeg'),img_median_blur)



cv2.imshow("img", img)
cv2.imshow("imgBlur", imgBlur)
cv2.imshow("imgGaussiaBlur", imgGausssianBlur)
cv2.imshow("img_median", img_median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
