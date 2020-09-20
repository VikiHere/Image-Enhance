'''
Spatial Filter
Vic S. 
 
 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image

def main(*arg):
    print("Format: python average_images.py *list of image names*")
    imgName = input("Please enter image name: ")

    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('L'), dtype='float')
    Image.open(imgName).convert('L').save("Lenna_grey.png")
    #Image.fromarray(img).show()
    h23 = np.array([ [1, 1, 1],      # filter kernel
                    [1, 4, 1],
                    [1, 1, 1]])
    
    h = (1/331)*np.array([  [1, 4, 7, 4, 1],
                            [4, 20, 33, 20, 4],
                            [7, 33, 55, 33, 7],
                            [4, 20, 33, 20, 4],
                            [1, 4, 7, 4, 1]
                            ])
    h2 = np.array([  [1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])
    out = spatial_filter(img, h).astype('uint8')
      
    final = Image.fromarray(out, mode='L')
    final.show()
    final.save("Lenna_blur.png")

# Spatial Filter,
def spatial_filter(img, h):
    padX = (int)(h.shape[0]/2)
    padY = (int)(h.shape[1]/2)

    # creating padded Image
    temp = np.zeros(shape=(2*padX + img.shape[0], 2*padY + img.shape[1]))
    temp[padX : img.shape[0]+padX , padY : img.shape[1]+padY] = img

    #final image
    out_img = np.zeros(shape=img.shape)

    # filter convolution
    for row in range(padX, img.shape[0]+padX):       # row
       for col in range(padY, img.shape[1]+padY):   # column

            startX = row - padX
            startY = col - padY
            endX = startX + h.shape[0]
            endY = startY + h.shape[1]
            window = temp[startX : endX, startY : endY]     #check if need to +1 for end 

            out_img[row - padX][col - padY] = (int)(np.sum(np.multiply(window, h)))
    
    return out_img

def chkOv(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i][j] > 255):
                img[i][j] = 255
            elif (img[i][j] < 0):
                img[i][j] = 0
    return img
if __name__ == '__main__':
    main()