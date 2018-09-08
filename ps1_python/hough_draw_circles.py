import numpy as np
import cv2
import math

def hough_draw_circles(img, outfile, peaks, radius):
    new_img = img.copy()

    for i in range(len(peaks)):
        a = peaks[i, 0]
        b = peaks[i, 1]
        if type(radius).__module__ == np.__name__:
            r = radius[i]
        else:
            r = radius
        #print(r)

        for x in range(img.shape[0]):
            if math.fabs(x - a) < r:
                temp = math.pow(r, 2) - math.pow((x - a), 2)
                y = b + math.sqrt(temp)
                if 0 < y < img.shape[1]:
                    new_img[x, int(y)] = 250

                y2 = b - math.sqrt(temp)
                if 0 < y2 < img.shape[1]:
                    new_img[x, int(y2)] = 250

    return new_img