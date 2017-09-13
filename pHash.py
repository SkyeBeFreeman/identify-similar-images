import math
import unittest

# 正则化图像
def regularizeImage(img, size = (32, 32)):
    return img.resize(size).convert('L')

# 获得图像像素矩阵
def getMatrix(img):
    matrix = []
    size = img.size
    for i in range(size[1]):
        pixel = []
        for j in range(size[0]):
            pixel.append(img.getpixel((j, i)))
        matrix.append(pixel)
    return matrix

# 计算系数矩阵
def getCoefficient(length):
    matrix = []
    sqr = 1.0 / math.sqrt(length)
    value = []
    for i in range(length):
        value.append(sqr)
    matrix.append(value)
    for i in range(1, length):
        value = []
        for j in range(0, length):
            value.append(math.sqrt(2.0 / length) * math.cos(i * math.pi * (j + 0.5) / length))
        matrix.append(value)
    return matrix

# 计算矩阵转秩
def getTranspose(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        value = []
        for j in range(len(matrix[i])):
            value.append(matrix[j][i])
        new_matrix.append(value)
    return new_matrix

# 计算矩阵乘法
def getMultiply(matrix1, matrix2):
    new_matrix = []
    for i in range(len(matrix1)):
        value = []
        for j in range(len(matrix2[i])): 
            ans = 0.0
            for h in range(len(matrix1[i])):
                ans += matrix1[i][h] * matrix2[h][j]
            value.append(ans)
        new_matrix.append(value)
    return new_matrix

# 计算DCT
def DCT(matrix):
    length = len(matrix)
    A = getCoefficient(length)
    AT = getTranspose(A)
    temp = getMultiply(A, matrix)
    DCT_matrix = getMultiply(matrix, AT)
    return DCT_matrix

# 计算左上角8*8并转化为list
def submatrix_list(matrix, size = (8, 8)):
    value = []
    for i in range(size[0]):
        for j in range(size[1]):
            value.append(matrix[i][j])
    return value

# 计算hash值
def getHashCode(sub_list):
    length = len(sub_list)
    mean = sum(sub_list) / length
    
    result = []
    for i in sub_list:
        if i > mean:
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

# 计算感知哈希算法相似度
def calpHashSimilarity(img1, img2):
    img1 = regularizeImage(img1)
    img2 = regularizeImage(img2)

    matrix1 = getMatrix(img1)
    matrix2 = getMatrix(img2)

    DCT1 = DCT(matrix1)
    DCT2 = DCT(matrix2)
    
    sub_list1 = submatrix_list(DCT1)
    sub_list2 = submatrix_list(DCT2)

    hc1 = getHashCode(sub_list1)
    hc2 = getHashCode(sub_list2)
    return compHashCode(hc1, hc2)

# 单元测试
class TestpHash(unittest.TestCase):
    def test_getHashCode(self):
        self.assertEqual(getHashCode([1, 2, 3]), [0, 0, 1])

if __name__ == '__main__':
    unittest.main()

__all__ = ['calpHashSimilarity']
