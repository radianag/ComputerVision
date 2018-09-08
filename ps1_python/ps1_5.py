#!/usr/bin/env python

import cv2
import numpy as np
from hough_circles_acc import *
from hough_peaks import *
from hough_draw_circles import *

img = cv2.imread('input/ps1-input1.png', 0)

blur = cv2.GaussianBlur(img, (7, 7), 2)
cv2.imwrite('output/ps1-5-a-1.png', blur)

edge2 = cv2.Canny(blur, 80, 170)
cv2.imwrite('output/ps1-5-a-2.png', edge2)

radius = 20
H = hough_circles_acc(edge2, radius)
#print(H)

normalizedImg = np.zeros(H.shape)
H_norm = cv2.normalize(H,  normalizedImg, 0, 255, cv2.NORM_MINMAX)

centers = hough_peaks(H, 10)

#print(centers)

new_img = hough_draw_circles(img, 'output/ps1-5-a-3.png', centers, radius)


x, y = find_circles(edge2, [20, 30])

print(y[0])
print(y[12])
new_img = hough_draw_circles(img, 'output/ps1-5-a-3.png', x, y)

#cv2.imshow('Hough Image', H_norm)

cv2.imshow('Drawn Image', new_img)
cv2.waitKey()
