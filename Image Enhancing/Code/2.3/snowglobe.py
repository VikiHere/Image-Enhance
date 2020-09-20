'''
Snowglobe Enhance
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
 NOTE: Make sure image 'snowglobe.png' is in the same location as this code
        no promts.
'''

import numpy as np
import sys
from PIL import Image
from adaptive_histogram import adaptive_histogram
#from clahe import clahe
from histogram_equalize import histogram_equalize
from laplacian_sharpen import laplacian_sharpen
from spatial_filter import spatial_filter
from unsharp_mask import unsharp_mask

def main(*arg):
    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open("snowglobe.png").convert('L'), dtype='float')
    #Image.open("noise_additive.png").convert('L').save("noise_additive_grey.png") #the images are grey but just in case

    out1 = unsharp_mask(img, 0.5, 0.5)
    out2 = unsharp_mask(img, 1, 1)
    #out3 = adaptive_histogram(img, 2, 2)
    out4 = histogram_equalize(img)
    out5 = laplacian_sharpen(img, 0.1)
    out6 = laplacian_sharpen(img, 0.2)
    #out7 = spatial_filter(img, h())
    #out8 = spatial_filter(img, h2())  


    final1 = Image.fromarray(out1, mode='L')
    final2 = Image.fromarray(out2, mode='L')
    #final3 = Image.fromarray(out3, mode='L')
    final4 = Image.fromarray(out4, mode='L')
    final5 = Image.fromarray(out5, mode='L')
    final6 = Image.fromarray(out6, mode='L')
    #final7 = Image.fromarray(out7, mode='L')
    #final8 = Image.fromarray(out8, mode='L')

    #final1.show()
    #final2.show()
    #final3.show()
    #final4.show()
    #final5.show()
    #final6.show()
    #final7.show()
    #final8.show()
    
    final1.save("snow_Unsharp0505.png")
    final2.save("snow_Unsharp_1_1.png")
    #final3.save("snow_AdapHist_2_2.png")
    final4.save("snow_HistEq_1.png")
    final5.save("snow_Lapa_0-1.png")
    final6.save("snow_Lapa_0-2.png")
    #final7.save("snow_Spatial_h1.png")
    #final8.save("snow_Spatial_h2.png")

def h():
    # Gaussian kernel with sigma = 1
    h = (1/331)*np.array([[1, 4, 7, 4, 1],[4, 20, 33, 20, 4],[7, 33, 55, 33, 7],[4, 20, 33, 20, 4],[1, 4, 7, 4, 1]])
    return h

def h2():
    h2 = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]])
    return h2

if __name__ == '__main__':
    main()