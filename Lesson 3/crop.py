import os
import cv2

# def mouse_callback(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(f"Posición del píxel: ({x}, {y})")
        
        
img = cv2.imread(os.path.join('..','data','bird.jpeg'))
# cv2.namedWindow('Imagen')
# cv2.setMouseCallback('Imagen', mouse_callback)

print(img.shape)
cv2.imshow("Imagen", img)

crop_img = img[150:200,420:490] 
cv2.imshow("Imagen2",crop_img)
cv2.waitKey(0)
