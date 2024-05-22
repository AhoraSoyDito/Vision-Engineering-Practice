import os.path as path
import numpy as np
import cv2

import numpy as np

img = cv2.imread(path.join('.','basket.jpg'))

img_edge = cv2.Canny(img, 80, 180)
img_d = cv2.dilate(img_edge, np.ones((5, 5), dtype=np.int8))
print(img.shape)

img_erode = cv2.erode(img_d, np.ones((5, 5), dtype=np.int8))



cv2.imshow('org', img)
cv2.imshow('edge', img_edge)
cv2.imshow('dilate', img_d)
cv2.imshow('erode', img_erode)
cv2.waitKey(0)

