import numpy as np
import cv2
import math

def find_bin(array, value):
    # for i in range(len(array)-1):
    #     if array[i] < value < array[i+1]:
    #         idx = i
    idx = np.searchsorted(array, value)
    return idx - 1

def hough_lines_acc(img, res=1, thetas=np.arange(-90, 89, 1)):

    array = np.zeros(img.shape)
    thet_len = len(thetas)
    vote = [[] for _ in range(thet_len)]
    #print(vote)

    # Find max Rho bin and space
    x = math.sqrt(math.pow(img.shape[0], 2) + math.pow(img.shape[1], 2))
    img_max = int(x) + 1
    rho = np.linspace(-img_max, img_max, int(img_max/res)+1)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            val = img[x, y]
            if val > 0:
                for h in range(thet_len):
                    var = x*math.cos(thetas[h]) + y*math.sin(thetas[h])
                    vote[h].append(var)

    #print(vote.shape)
    print(len(vote))

    H = np.zeros((len(rho), thet_len), np.uint8) #Row rho, #Column thetas
    #Put in bins
    for i in range(len(vote)):
        for j in range(len(vote[0])):
            idx = find_bin(rho, vote[i][j])
            H[idx, i] += 1

    print(H.shape)
    print(max(H[100]))
    # p = inputParser()
    # addParameter(p, 'RhoResolution', 1)
    # addParameter(p, 'Theta', linspace(-90, 89, 180))
    # parse(p, varargin{:})
    #
    # rhoStep = p.Results.RhoResolution
    # theta = p.Results.Theta

    return H, thetas, rho