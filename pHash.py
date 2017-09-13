import math

# 正则化图像
def regularizeImage(img, size = (32, 32)):
    return img.resize(size).convert('L')

# 获得图像像素矩阵
def getMatrix(img):
    matrix = []
    size = img.size
    for i in range(size[1]):
        pixel = []
        for j in range[0]:
            pixel.append(img.getpixel(j, i))
        matrix.append(pixel)
    return matrix

# 计算系数矩阵
def getCoefficient(length):
    matrix = []
    sqr = math.sqrt(1 / length)
    value = []
    for i in range(length):
        value.append(sqr)
    matrix.append(value)
    for i in range(1, length):
        value = []
        for j in range(0, n):
            value.append(math.sqrt(2.0 / length) * math.cos(i * math.pi * (j + 0.5) / length))
        matrix.append(value)

# 计算感知哈希算法相似度
def calpHashSimilarity(img1, img2):
    img1 = regularizeImage(img1)
    img2 = regularizeImage(img2)

    matrix1 = getMatrix(img1)
    matrix2 = getMatrix(img2)

    DCT1 = DCT(matrix1)
    DCT2 = DCT(matrix2)
    

    hc1 = getHashCode(img1)
    hc2 = getHashCode(img2)
    return compHashCode(hc1, hc2)

if __name__ == '__main__':
    matrix = [[1,2], [3, 4]]
    print(len(matrix))