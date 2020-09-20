'''
Adaptive Histogram (Local Histogram Equalization)
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image

def main(*arg):
    imgName = input("Please enter image name: ")
    h = (int)(input("Height of kernel: "))
    w = (int)(input("Width of kernel: "))

    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('L'), dtype='uint32')
    #Image.open(imgName).convert('L').save("Lenna_grey.png")

    out = adaptive_histogram(img, h, w).astype('uint8')
      
    final = Image.fromarray(out, mode='L')
    final.show()
    final.save("local_hist_eq.png")

def adaptive_histogram(img, H, W):
    print("...working, note: this operation takes ~50s for an image of ~500x500px with 5x5 kernel (i5 @ 3.1GHz)...")

    padX = (int)(H/2)
    padY = (int)(W/2)

    # creating padded Image
    temp = np.zeros(shape=(2*padX + img.shape[0], 2*padY + img.shape[1]))
    temp[padX : img.shape[0] + padX, padY : img.shape[1] + padY] = img

    #final image
    out_img = np.zeros(img.shape, dtype='uint32')

    # sliding the window accross the image
    for row in range(padX, img.shape[0]+padX):       # row
       for col in range(padY, img.shape[1]+padY):    # column
            startX = row - padX
            startY = col - padY
            endX = row + padX
            endY = col + padY
            window = temp[startX : endX+1, startY : endY+1]
            
            out_img[row-padX][col-padY] = window_hist_equal(window.astype('uint8'), temp[row-padX][col-padY].astype('uint32'))
    
    return out_img


def window_hist_equal(win, in_pixel):
    # num of pixels
    pixels = win.shape[0] * win.shape[1]
    
    # Initial histogram
    lut = np.zeros(256, dtype="float")

    # Get histogram
    for row in range(win.shape[0]):
        for col in range(win.shape[1]):
            #print(win[row][col])

            lut[win[row][col]] += 1

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

    return np.rint(cdf[in_pixel])

if __name__ == '__main__':
    main()