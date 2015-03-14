import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters
from skimage.color import rgb2grey

def show_three(im1, im2, im3):
    fig, ax = plt.subplots(1, 3, sharey=True)
    ax[0].imshow(im1)
    ax[1].imshow(im2)
    ax[2].imshow(im3)
    fig.show()

def show_four(im1, im2, im3, im4):
    fig, ax = plt.subplots(2, 2, sharex = True, sharey=True)
    ax[0,0].imshow(im1)
    ax[0,1].imshow(im2)
    ax[1,0].imshow(im3)
    ax[1,1].imshow(im4)
    fig.show()

def get_intensity(rgb_im):
    return rgb2grey(rgb_im)

def threshold(im, n_stddev):
    avg = np.mean(np.abs(im))
    std = np.std(np.abs(im))
    result = np.zeros(shape = im.shape)
    result[np.abs(im) > (avg + n_stddev*std)] = 1
    return result
