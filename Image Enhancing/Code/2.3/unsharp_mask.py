'''
Unsharpen Mask
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
import math
from PIL import Image
from spatial_filter import spatial_filter, chkOv

def main(*arg):
    imgName = input("Please enter image name: ")
    r = (float)(input("Radius of blurring kernel: "))
    k = (float)(input("Strength of the mask: "))

    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('L'), dtype='float')

    out = unsharp_mask(img, r, k).astype('uint8')
      
    final = Image.fromarray(out, mode='L')
    final.show()
    final.save("unsharp_mask_result.png")

def unsharp_mask(img, r, k):
    # Creating the Gaussian kernel
    sigma = r/3
    N = (int)(r*2)
    kernel = np.fromfunction(lambda x, y: (1/(2*math.pi*sigma**2)) * math.e ** ((-1*((x-(N-1)/2)**2+(y-(N-1)/2)**2))/(2*sigma**2)), (N, N))
    kernel /= np.sum(kernel)

    # Applying Gaussian Filter
    blur_img = np.zeros(shape=img.shape, dtype='float')
    blur_img = spatial_filter(img, kernel)
    
    # Getting the mask
    mask = np.subtract(img, blur_img)

    # Returning the sharpened image
    return chkOv(np.add(np.multiply(mask,k), img)).astype('uint8')

if __name__ == '__main__':
    main()