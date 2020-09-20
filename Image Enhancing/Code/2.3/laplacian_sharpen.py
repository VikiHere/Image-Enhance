'''
Laplacian Sharpen
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image
from spatial_filter import spatial_filter, chkOv

def main(*arg):
    imgName = input("Please enter image name: ")
    k = (float)(input("Strength of the mask: "))

    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('L'), dtype='float')

    out = laplacian_sharpen(img, k).astype('uint8')
      
    final = Image.fromarray(out, mode='L')
    final.show()
    final.save("laplacian_sharpen.png")

def laplacian_sharpen(img, k):

    # Laplacian Kernel
    kernel = np.array([  [-1, -1, -1],
                         [-1, 8, -1],
                         [-1, -1, -1]
                         ])

    # Applying Laplacian
    e_map = np.zeros(shape=img.shape, dtype='float')
    e_map = spatial_filter(img, kernel)

    # Returning the sharpened image
    return chkOv(np.add(np.multiply(e_map,abs(k)), img)).astype('uint8')

if __name__ == '__main__':
    main()