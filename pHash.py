# 正则化图像
def regularizeImage(img, size = (32, 32)):
    return img.resize(size).convert('L')

# 计算感知哈希算法相似度
def calpHashSimilarity(img1, img2):
    img1 = regularizeImage(img1)
    img2 = regularizeImage(img2)
    hc1 = getHashCode(img1)
    hc2 = getHashCode(img2)
    return compHashCode(hc1, hc2)