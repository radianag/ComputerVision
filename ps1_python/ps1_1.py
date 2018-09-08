#!/usr/bin/env python

import cv2
import numpy as np


#Problem 1
img = cv2.imread('input/ps1-input0.png',0)
edge = cv2.Canny(img, 100, 150)

nol = np.zeros(img.shape, np.uint8)

cv2.imwrite('output/ps1-1-a-1.png', edge)

print(edge.shape[1])
cv2.imshow('image', edge)
cv2.waitKey()

