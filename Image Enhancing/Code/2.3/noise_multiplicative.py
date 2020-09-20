'''
Noise Multiplicative Enhance
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
 NOTE: Make sure image 'noise_multiplicative.png' is in the same location as this code
        no promts.
'''

import math
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
    img = np.asarray(Image.open("noise_multiplicative.png").convert('L'), dtype='float')

    # Creating the Gaussian kernel
    r = 4
    sigma = r/3
    N = (int)(r*2)
    kernel = np.fromfunction(lambda x, y: (1/(2*math.pi*sigma**2)) * math.e ** ((-1*((x-(N-1)/2)**2+(y-(N-1)/2)**2))/(2*sigma**2)), (N, N))
    kernel /= np.sum(kernel)

    # Applying Gaussian Filter
    blur_img = np.zeros(shape=img.shape, dtype='uint8')
    blur_img = spatial_filter(img, kernel).astype('uint8')
    out1 = laplacian_sharpen(blur_img, 0.1)
    out = unsharp_mask(out1, 1, 1)

    
    final2 = Image.fromarray(out, mode='L')

    final2.show()

    final2.save("noiseMul_gauss_2sharp.png") 


def h():
    # Gaussian kernel with sigma = 1
    h = (1/331)*np.array([[1, 4, 7, 4, 1],[4, 20, 33, 20, 4],[7, 33, 55, 33, 7],[4, 20, 33, 20, 4],[1, 4, 7, 4, 1]])
    return h

def h2():
    h2 = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]])
    return h2

if __name__ == '__main__':
    main()