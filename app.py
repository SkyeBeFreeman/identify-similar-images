from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def regularizeImage(img, size = (256, 256)):
    return img.resize(size).convert('RGB')

def calHistogramSimilarity(hg1, hg2):
    if len(hg1) != len(hg2):
        raise Exception('样本点个数不一样')
    sum = 0
    for x1, x2 in zip(hg1, hg2):
        if x1 != x2:
            sum += 1 - float(abs(x1 - x2) / max(x1, x2))
        else:
            sum += 1
    return sum / len(hg1)

if __name__ == '__main__':

    # read regularized images
    img1 = regularizeImage(Image.open('img1.jpg'))
    img2 = regularizeImage(Image.open('img2.jpg'))
    
    # img1.show()
    # img2.show()

    hg1 = img1.histogram()
    # print(img1.histogram())
    print('img1的样本点有', len(hg1), '个')

    hg2 = img2.histogram()
    # print(img2.histogram())
    print('img2的样本点有', len(hg2), '个')

    # draw the histogram
    plt.plot(range(len(hg1)), hg1, color='blue', linewidth=1.5, label='img1')
    plt.plot(range(len(hg2)), hg2, color='red', linewidth=1.5, label='img2')
    plt.legend(loc='upper left')
    # plt.show()

    # print the similarity
    print(calHistogramSimilarity(hg1, hg2))
