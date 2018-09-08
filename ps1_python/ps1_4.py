#!/usr/bin/env python

import cv2
import numpy as np
from hough_lines_acc import *
from hough_peaks import *
from hough_lines_draw import *

img = cv2.imread('input/ps1-input1.png', 0)
blur = cv2.GaussianBlur(img, (7, 7), 2)

cv2.imwrite('output/ps1-4-a-1.png', blur)
edge2 = cv2.Canny(blur, 80, 170)

cv2.imwrite('output/ps1-4-b-1.png', edge2)

# cv2.imshow('image2', edge2)
# cv2.waitKey()

H, theta, rho = hough_lines_acc(edge2, res=1, thetas=np.arange(-90, 89, 0.6))
cv2.imwrite('output/ps1-4-c-1.png', H)
peaks = hough_peaks(H, 8)
hough_lines_draw(img, 'output/ps1-4-c-2.png', peaks, rho, theta)


