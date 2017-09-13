# 正则化图像
def regularizeImage(img, size = (9, 8)):
    return img.resize(size).convert('L')

# 计算hash值
def getHashCode(img, size = (9, 8)):

    result = []
    for i in range(size[0] - 1):
        for j in range(size[1]):
            current_val = img.getpixel((i, j))
            next_val = img.getpixel((i + 1, j))
            if current_val > next_val:
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

# 计算差异哈希算法相似度
def caldHashSimilarity(img1, img2):
    img1 = regularizeImage(img1)
    img2 = regularizeImage(img2)
    hc1 = getHashCode(img1)
    hc2 = getHashCode(img2)
    return compHashCode(hc1, hc2)

__all__ = ['caldHashSimilarity']