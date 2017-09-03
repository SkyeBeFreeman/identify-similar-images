# 正则化图像
def regularizeImage(img, size = (8, 8)):
    return img.resize(size).convert('L')

# 计算hash值
def getHashCode(img, size = (8, 8)):

    pixel = []
    for i in range(size[0]):
        for j in range(size[1]):
            pixel.append(img.getpixel((i, j)))

    avg = sum(pixel) / len(pixel)

    result = []
    for i in pixel:
        if i > avg:
            result.append(1)
        else:
            result.append(0)
    
    return result

# 比较hash值
def compHashCode(hc1, hc2):
    cnt = 0
    for i, j in zip(hc1, hc2):
        if i == j:
            cnt += 1
    return cnt

def calaHashSimilarity(img1, img2):
    img1 = regularizeImage(img1)
    img2 = regularizeImage(img2)
    hc1 = getHashCode(img1)
    hc2 = getHashCode(img2)
    return compHashCode(hc1, hc2)

__all__=['calaHashSimilarity']
