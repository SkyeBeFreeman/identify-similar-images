from PIL import Image
from multiprocessing import Process
import histogram as htg
import aHash as ah

if __name__ == '__main__':

    # read image files
    img1 = Image.open('img1.jpg')
    img2 = Image.open('img2.jpg')
    # img1.show()
    # img2.show()

    # regularize the images
    img1_htg = htg.regularizeImage(img1)
    img2_htg = htg.regularizeImage(img2)
    
    hg1 = img1_htg.histogram()
    # print(img1.histogram())
    print('img1的样本点有', len(hg1), '个')
    hg2 = img2_htg.histogram()
    # print(img2.histogram())
    print('img2的样本点有', len(hg2), '个')

    # draw the histogram in a no-blocking way
    sub_thread = Process(target=htg.drawHistogram, args=(hg1, hg2,))
    sub_thread.start()

    # print the histogram similarity
    print('依据图片直方图距离计算相似度：', htg.calMultipleHistogramSimilarity(img1_htg, img2_htg))
