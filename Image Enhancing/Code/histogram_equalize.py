import numpy as np
import sys
from PIL import Image

def hist(img):
    #Calculates normalized histogram of an image
    xSize = int((img.shape[0]))
    ySize = int((img.shape[1]))    
    
    imgFlat = img.flatten()
    #array of size 256, filled with zeros
    histogram = np.zeros(256) 

    #print(type(imgFlat))
    #print(len(imgFlat))

    #Loop through flatten image and count the occurances of that pixel
    for i in imgFlat.astype(int): 
        histogram[i] += 1
    #print(histogram[204])

    return histogram


def cums(i):
    i = iter(i)
    n = [next(i)]

    for j in i:
        n.append(n[-1] + j)

    #print(len(n))
    #print(n[0])
    #print(n[50])
    #print(n[150])
    #print(n[255])

    return np.array(n)


#out = histogram_equalize(img)
#Result histogram shoudl fill 0 - 255 range
#need to apply a transform to every pixel in the image
def histogram_equalize(img):
    imgFlat = img.flatten()
    imgHist = hist(img)
    cumsum = cums(imgHist)

    #Re-normalize cumulative sum values to a range between 0 - 255
    numer = (cumsum - cumsum.min()) * 255
    denom = cumsum.max() - cumsum.min()

    #re-normalize the cdf
    cumsum = numer/denom
    cumsum = cumsum.astype('uint8')

    #print (len(cumsum))
    #print (cumsum[50])
    #print (cumsum[255])

    #print(type(imgFlat[4]))
    #print(imgFlat[130])

    imgEqu = cumsum[imgFlat.astype('uint8')]

    #unflatten the new image
    #imgEqu = np.reshape(imgEqu, imgEqu.shape)
    imgEqu = np.reshape(imgEqu, img.shape)

    return imgEqu


if __name__ == '__main__':
    imgName = input("Name of Image: ")

    imgInput = np.asarray(Image.open(imgName).convert('L'), dtype='float')
    Image.open(imgName).convert('L').save("Test_grey.png")
    #Type is float 

    #xSize = (imgInput.shape[0])
    #ySize = (imgInput.shape[1])

    #imgHist = hist(imgInput)
    #cumsum = cums(imgHist)

    out_img = histogram_equalize(imgInput)

    print(type(out_img[1][4]))

    #eqImg = Image.fromarray(out_img.astype('uint8'), mode='L')
    eqImg = Image.fromarray(out_img,'L')
    eqImg.show()
    eqImg.save("Equalized_Histogram.png")



