import numpy as np
import cv2
import math


def hough_lines_draw(img, outfile, peaks, rho, theta):
    i = 0

    new_img = img.copy()

    #print(len(peaks))
    for i in range(len(peaks)):
        a = rho[int(peaks[i, 0])]
        b = theta[int(peaks[i, 1])]
        print(b)

        if b == 0:
            for y in range(img.shape[1]):
                temp = a - y * math.sin(b)
                x = int(temp/math.cos(b))

                if (0 < x < img.shape[0]):
                    new_img[x, y] = 250
        else:
            for x in range(img.shape[0]):
                temp = a - x * math.cos(b)
                y = int(temp/math.sin(b))

                if (0 < y < img.shape[1]):
                    new_img[x, y] = 250

    cv2.imwrite(outfile, new_img)
    cv2.imshow('imga', new_img)
    cv2.waitKey()
