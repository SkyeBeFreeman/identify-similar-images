from PIL import Image
from multiprocessing import Process
import histogram as htg

def regularizeImage(img, size = (256, 256)):
    return img.resize(size).convert('RGB')

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

    # draw the histogram with no-blocking
    sub_thread = Process(target=htg.drawHistogram, args=(hg1, hg2,))
    sub_thread.start()

    # print the similarity
    print('依据图片直方图距离计算相似度：', htg.calMultipleHistogramSimilarity(img1, img2))
