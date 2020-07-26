import cv2
import numpy as np

img = cv2.imread('T.png', 1)

#itta special T, highlight krna to banta hai
img = cv2.circle(img, (380, 520), 70, (0, 255, 0), 5, cv2.LINE_AA )

rows, cols, ch = img.shape
print(rows, cols)
for i in range(1,5):
    matrix = np.float32([[1, 0 , 30*(-1**i) *i], [0, 1, 20*(-1**i) *i]])
    trans_img = cv2.warpAffine(img, matrix, (cols, rows))
    cv2.imshow('Translated_img{}'.format(i), trans_img)

for i in range(1,5):
    matrix_r = cv2.getRotationMatrix2D((cols/2, rows/2), i*i*30, 0.25*i)
    rotate_img = cv2.warpAffine(img, matrix_r, (cols, rows))
    cv2.imshow('Rotated_img{}'.format(i), rotate_img)

# Let's blurrr....
Guass_blur = cv2.GaussianBlur(img,(5,5),0)
Bila_blur = cv2.bilateralFilter(img,9,75,75)   # :)

cv2.imshow('T G smooothing', Guass_blur)
cv2.imshow('T B smooothing', Bila_blur)

cv2.imshow('T orginiala', img)

k = cv2.waitKey(0)
cv2.destroyAllWindows()