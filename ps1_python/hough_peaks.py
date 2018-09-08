import numpy as np
import cv2
import math
def last(n):
    m = 0
    return n[m]

def hough_peaks(H, numpeaks):
    H_max = np.amax(H)

    test = H_max
    #print("number:" + str(test))

    peaks = ([] ,[] )
    while len(peaks[0]) < numpeaks:
        peaks = np.where(H > test)
        #print(len(peaks[0]))
        test = test - 0.5
        #print(peaks)
    #peach = np.zeros(len(peaks[0]))

    peach = [None]*len(peaks[0])
    He = np.zeros(len(peaks[0]))

    for i in range(len(peaks[0])):
        peach[i] = (H[peaks[0][i], peaks[1][i]], peaks[0][i], peaks[1][i])
        #[i] =

    #print('before:', peach)
    #m = 0
    ge = sorted(peach, key=last, reverse=True)

    stuff = np.zeros((numpeaks,2))
    for i in range(numpeaks):
        stuff[i, :] = [ge[i][1], ge[i][2]]

    #print(stuff.shape)

    return stuff