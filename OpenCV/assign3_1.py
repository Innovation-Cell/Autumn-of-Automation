#LET'S FALL IN LOVE WITH IMAGES!!!!

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)


lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

lap = np.uint8(np.absolute(lap))
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelcombine = cv2.bitwise_or(sobelX, sobelY)

image = [img, lap, sobelX, sobelY, sobelcombine]
titles = ['Original', 'Laplacion', 'sobelX', "sobelY", "sobelcombine"]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

