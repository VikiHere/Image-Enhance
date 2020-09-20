'''
Contrast Limited Adaptive Histogram Equalization (Local Histogram Equalization)
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
    cutoff = (int)(input("Bin cutoff (enter '-1' if you don't want to use CLAHE): "))

    if (cutoff != -1):
        print("..............")
        print("WARNING: CLAHE mode; for Goats 500x500px/15x15 kernel/cutoff = 3, approx. ETA = 2 min")
        print("\t for Plane 512x512px/15x15 kernel/cutoff = 2, approx. ETA = ** 10 min! **")
        print("...this can take long, sorry Ryan... ) : ")
        print("..............")

    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('L'), dtype='uint32')

    out = adaptive_histogram(img, h, w, cutoff).astype('uint8')
      
    final = Image.fromarray(out, mode='L')
    final.show()
    final.save("CLAHE_result.png")

def adaptive_histogram(img, H, W, cutoff):
    print("...working, note: this operation takes ~50s for an image of ~500x500px (i5 @ 3.1GHz)...")

    padX = (int)(H/2)
    padY = (int)(W/2)

    # Making sure 
    if (cutoff <= (H*W)/256 and cutoff != -1):
        cutoff = -1
        print("Attention: cutoff smaller than " + (str)(H*W/256) + ", thus not using CLAHE!")

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
            
            out_img[row-padX][col-padY] = window_hist_equal(window.astype('uint8'), temp[row-padX][col-padY].astype('uint32'),cutoff)
    
    return out_img


def window_hist_equal(win, in_pixel, cutoff):
    # num of pixels
    pixels = win.shape[0] * win.shape[1]

    # Initial histogram
    lut = np.zeros(256, dtype="float")

    over_cutoff = 0

    # Get histogram
    for row in range(win.shape[0]):
        for col in range(win.shape[1]):
            
            if (cutoff != -1 and lut[win[row][col]] >= cutoff):
                over_cutoff += 1    # *** CLAHE: Get number of items above cutoff 
            else:
                lut[win[row][col]] += 1
    #print(win)
    # *** CLAHE: Get number of additional pixels to add per bin, and add them
    if (cutoff != -1):
        
        # if number of extra pixel values is smaller than number of pixels in window
        if (over_cutoff < pixels):      
            for i in range(over_cutoff):          # add them to the smallest bins
                #print(np.nonzero(lut))
                index = np.argmin(np.nonzero(lut))
                #print(index)
                #print(index.shape)
                lut[index] += 1
        else:
            # if number of extra pixel values is biggern than num. of pixels in window
            over_cutoff = np.rint(over_cutoff / pixels)
            lut = lut + over_cutoff

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