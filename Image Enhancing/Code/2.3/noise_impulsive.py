'''
Noise Impulsive Enhance
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
 NOTE: Make sure image 'noise_impulsive.png' is in the same location as this code
        no promts.
'''

import numpy as np
import sys
from PIL import ImageFilter
from PIL import Image
from adaptive_histogram import adaptive_histogram
from histogram_equalize import histogram_equalize
from laplacian_sharpen import laplacian_sharpen
from spatial_filter import spatial_filter
from unsharp_mask import unsharp_mask

def main(*arg):
    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open("noise_impulsive.png").convert('L'), dtype='float')

    simg = Image.open("noise_impulsive.png")
    dimg = simg.filter(ImageFilter.ModeFilter(size=5))
    
    dimg.save("test.png");
    img2 = np.asarray(Image.open("test.png").convert('L'), dtype='float')
    out = unsharp_mask(img2, 2,2)

    final = Image.fromarray(out, mode='L')
    final.show()

    final.save("noiseImp_median_unsharp.png")

def h():
    # Gaussian kernel with sigma = 1
    h = (1/331)*np.array([[1, 4, 7, 4, 1],[4, 20, 33, 20, 4],[7, 33, 55, 33, 7],[4, 20, 33, 20, 4],[1, 4, 7, 4, 1]])
    return h

def h2():
    h2 = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]])
    return h2

if __name__ == '__main__':
    main()