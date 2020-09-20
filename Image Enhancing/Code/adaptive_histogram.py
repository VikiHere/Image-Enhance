import numpy as np
import sys
from PIL import Image
from histogram_equalize import histogram_equalize

def window_block(arr, rows, cols):
    y, x = arr.shape
    
    assert y % rows == 0, "{} rows is not evenly divisble by {}".format(h, nrows)
    assert x % cols == 0, "{} cols is not evenly divisble by {}".format(w, ncols)
    
    newWindow = arr.reshape(y//rows, rows, -1, cols).swapaxes(1,2).reshape(-1, rows, cols))

    return newWindow

def adaptive_histogram(img, H, W):
    xSize = (imgInput.shape[0])
    ySize = (imgInput.shape[1])

    #print(xSize) #321
    #print(ySize) #481

    if (ySize%H == 0):
        if (xSize%W == 0):
            #Splitting the image into window sizes
            for i in range(ySize/H):
                for j in range(xSize/W):
                    #creating the window sizes
                    tempy = 


        elif (xSize%W != 0):
    elif (ySize%H != 0):
        if (xSize%W == 0):
            #creating the window size
        elif (xSize%W != 0):


if __name__ == '__main__':
    imgName = input("Name of Image: ")

    imgInput = np.asarray(Image.open(imgName).convert('L'), dtype='float')
    Image.open(imgName).convert('L').save("Test_grey.png")
    #Type is float 

    out_img = adaptive_histogram(imgInput, 8, 8)