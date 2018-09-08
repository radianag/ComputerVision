#!/usr/bin/env python

import cv2
import numpy as np


'''
Problem Set 0: Images as Functions
'''

if __name__ == '__main__':
    img1 = cv2.imread('input/lena.jpg', cv2.IMREAD_COLOR)
    cv2.imwrite('output/ps0-1-a-1.png', img1)

    img2 = cv2.imread('input/woman.tiff', cv2.IMREAD_COLOR)
    cv2.imwrite('output/ps0-1-a-2.png', img2)

    #Swap blue and red channels
    img1_swapped = img1.copy()
    img1_swapped[:, :, 0] = img1[:, :, 2]
    img1_swapped[:, :, 2] = img1[:, :, 0]
    cv2.imwrite('output/ps0-2-a-1.png', img1_swapped)

    # Create a monochrome image (img1_green) by selecting the green channel of image 1
    # Output: ps0-2-b-1.png
    img1_green = img1[:, :, 1]
    cv2.imwrite('output/ps0-2-b-1.png', img1_green)

    img1_red = img1[:, :, 2]
    cv2.imwrite('output/ps0-2-c-1.png', img1_red)



    #Problem 3, Monochrome Swaps
    img1_size = img1.shape
    print(img1_size)
    cr_size = 100
    ce_x_min = (img1_size[0]-1)/2-cr_size/2
    ce_x_max = (img1_size[0] - 1) / 2 + cr_size / 2

    ce_y_min = (img1_size[1]) / 2 - cr_size / 2
    ce_y_max = (img1_size[1]) / 2 + cr_size / 2

    img1_cropped = img1_green[ce_x_min:ce_x_max, ce_y_min: ce_y_max]
    print(img1_cropped.shape)


    img2_size = img2.shape
    print(img2_size)

    img2_green = img2[:, :, 1]
    ce_x_min = (img2_size[0] - 1) / 2 - cr_size / 2
    ce_x_max = (img2_size[0] - 1) / 2 + cr_size / 2

    ce_y_min = (img2_size[1]) / 2 - cr_size / 2
    ce_y_max = (img2_size[1]) / 2 + cr_size / 2

    img2_green[ce_x_min:ce_x_max, ce_y_min: ce_y_max] = img1_cropped



    #img1_green_cr = img1_green []

    # Problem 4 a
    max1 = img1_green.max()
    min1 = img1_green.min()
    mean = img1_green.mean()
    std = img1_green.std()

    print('4a) img1_green: min = %d, max =%d, mean = %f, std = %f' % (min1, max1, mean, std))

    # Problem 4b, Do stuff
    img1_green_normed = cv2.add(cv2.multiply(cv2.divide(cv2.subtract(img1_green.copy(), mean), std), 10), mean)


    # Probelm 4c, Shift cells to right
    x = img1_green.copy()
    img1_shift = np.ones(img1_green.shape, np.uint8) * 255
    img1_shift[:, 2:] = x[:, :-2]

    # Problem 4d,
    img1_sub = cv2.subtract(img1_green.copy(), img1_shift)


    # Problem 5, Gaussian Noise
    # a) Green Channel
    noise = np.random.normal(size=img1_green.shape, scale=5)
    noisy_img1_g = img1.copy()
    noisy_img1_g[:, :, 1] = noisy_img1_g[:, :, 1] + noise

    # b) Blue Channel
    noise2 = np.random.normal(size=img1_green.shape, scale=5)
    noisy_img1_b = img1.copy()
    noisy_img1_b[:, :, 0] = noisy_img1_b[:, :, 0] + noise2

    cv2.imshow('image', noisy_img1_b)
    cv2.waitKey()


