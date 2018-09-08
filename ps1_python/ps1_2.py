#!/usr/bin/env python

import cv2
import numpy as np

import time
from hough_lines_acc import *
from hough_peaks import *
from hough_lines_draw import *

#1.
img = cv2.imread('input/ps1-input0.png', 0)
edge = cv2.Canny(img, 100, 200)

cv2.imwrite('output/ps1-1-a-1.png', edge)

H, theta, rho = hough_lines_acc(edge, res=0.2, thetas=np.arange(-90, 89, 0.5))
cv2.imwrite('output/ps1-2-a-1.png', H)

peaks = houghpeaks(H, 10)
cv2.imwrite('output/ps1-2-b-1.png', peaks)

hough_lines_draw(img, 'output/ps1-2-c-1.png', peaks, rho, theta)

# cv2.imshow('image', img)
# cv2.waitKey()
