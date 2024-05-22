import cv2 
import os.path as path
import numpy as np

perry = cv2.imread(path.join('.', 'salt-perry.png'))

k_sizes = 4
#imgBlur = cv2.blur(img,(k_size, k_size))
#!--- Normal Blur 
perry_blur = cv2.blur(perry, (k_sizes, k_sizes))
cv2.imwrite(path.join('.', 'perry_blur.png'), perry_blur)

#!--- Gaussian Blur 
perry_gaussian = cv2.GaussianBlur(perry, (k_sizes, k_sizes), 3)
cv2.imwrite(path.join('.', 'perry_gaussian.png'), perry_gaussian)

#!--- Median Blur 
perry_median = cv2.medianBlur(perry, (k_sizes))
cv2.imwrite(path.join('.', 'perry_median.png'), perry_median)

cv2.imshow('perry_slat', perry)
cv2.imshow('perry_blur',perry_blur)
cv2.imshow('perry_gaussian',perry_gaussian)
cv2.imshow('perry_median',perry_median)

cv2.waitKey(0)
cv2.destroyAllWindows()