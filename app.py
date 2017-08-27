from PIL import Image
import numpy as np

def regularizePicture(img, size = (256, 256)):
    return img.resize(size).convert('RGB')

if __name__ == '__main__':

    img1 = Image.open('img1.jpg')
    img2 = Image.open('img2.jpg')
    
    # img1.show()
    # img2.show()

    print(img1.histogram())
    print(len(img1.histogram()))
    # img2.histogram()
