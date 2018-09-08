import numpy as np
import cv2
import math
from hough_peaks import *

def hough_circles_acc(img, radius=1):
    r = radius
    theta = 10

    a_max = img.shape[0]
    b_max = img.shape[1]
    H = np.zeros((a_max, b_max), np.uint8)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            val = img[x, y]
            if val > 0:
                for a in range(img.shape[0]):
                    if math.fabs(x-a) < r:
                        temp = math.pow(r, 2) - math.pow((x-a), 2)
                        #print(temp)
                        b = y - math.sqrt(temp)
                        b_int = round(b)
                        if 0 < b_int < img.shape[1]:
                            H[a, int(b_int)] += 1

                        b = y + math.sqrt(temp)
                        b_int = round(b)
                        if 0 < b_int < img.shape[1]:
                            H[a, int(b_int)] += 1

                # for b in range(img.shape[1]):
                #     if math.fabs(y-b) < r:
                #         temp = math.pow(r, 2) - math.pow((y-b), 2)
                #         #print(temp)
                #         a = x - math.sqrt(temp)
                #         a_int = round(a)
                #         if 0 < a_int < img.shape[1]:
                #             H[int(a_int), b] += 1

    return H


def find_circles(img_edges, radii = [20, 30]):
    rad = np.arange(radii[0], radii[1]+1, 1)

    peaks = 10
    centers = np.zeros((len(rad) * peaks, 2))
    radius = np.zeros((len(rad) * peaks))
    #print(centers)
    for i in range(len(rad)):
        H = hough_circles_acc(img_edges, rad[i])
        center_temp = hough_peaks(H, peaks)

        #print(center_temp.shape)
        centers[i*peaks: (i+1)*peaks, :] = center_temp
        radius[i*peaks: (i+1)*peaks] = np.full(peaks, rad[i])
    return centers, radius