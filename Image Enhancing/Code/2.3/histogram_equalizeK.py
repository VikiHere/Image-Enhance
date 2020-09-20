'''
 Histogram Equalization
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image

def main(*arg):
    imgName = input("Please enter image name: ")

    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('L'), dtype='uint8')
    #Image.open(imgName).convert('L').save("Lenna_grey.png")

    out = histogram_equalize(img).astype('uint8')
      
    final = Image.fromarray(out, mode='L')
    final.show()
    final.save("global_equalization.jpg")

def histogram_equalize(img):
    # num of pixels
    pixels = img.shape[0] * img.shape[1]

    # Initial histogram
    lut = np.zeros(256, dtype="float")

    # Get histogram
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            lut[img[row][col]] += 1

    # Get the PDF from the histogram
    lut = np.divide(lut, pixels)
    cdf = np.zeros(shape=lut.shape)

    # Get the CDF
    for i in range(cdf.shape[0]):
        if (i == 0):
            cdf[i] = lut[i]
        else:
            cdf[i] = lut[i] + cdf[i-1]

    # Multiply CDF by max intensity range to equalize
    cdf = np.multiply(cdf, 255)

    # Make final LUT and round the values
    lut_f = np.zeros(shape=lut.shape, dtype="uint8") 
    lut_f = np.rint(cdf)

    out_img = np.zeros(shape=img.shape)

    # Apply final LUT to the image
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            out_img[row][col] = lut_f[img[row][col]]

    return out_img

if __name__ == '__main__':
    main()