from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def regularizePicture(img, size = (256, 256)):
    return img.resize(size).convert('RGB')

if __name__ == '__main__':

    img1 = Image.open('img1.jpg')
    img2 = Image.open('img2.jpg')
    
    # img1.show()
    # img2.show()

    hg1 = img1.histogram()
    # print(img1.histogram())
    print('img1 样本点有', len(hg1))

    hg2 = img2.histogram()
    # print(img2.histogram())
    print('img2 样本点有', len(hg2))

    plt.plot(range(len(hg1)), hg1, range(len(hg2)), hg2)
    plt.show()
