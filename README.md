# Identify similar images

- 利用直方图距离计算图片相似度

计算公式：

<img src="http://chart.googleapis.com/chart?cht=tx&chl=Sim(G,S)=\frac{1}{N}\sum_{i=1}^{N}{(1-\frac{|g_i-s_i|}{Max(g_i,s_i)})}" style="border:none;">

其中，G和S为两张图片的图像颜色分布直方图，N为颜色空间样点数。

这里使用分块的方法计算相似度，用以提高各部分的特征，防止图片颜色相似导致计算的相似度高。

- 利用平均哈希算法计算图片相似度

计算步骤：

1. 缩放图片：一般大小为8*8，64个像素值
2. 简化色彩，转化为灰度图：可以使用Image的convert('L')方法
3. 计算平均值：计算出灰度图所有像素点的像素值的平均值
4. 比较像素灰度值：遍历灰度图的每一个像素值与上一步计算的平均值，大于平均值记录为1，否则为0
5. 得到64位图像指纹
6. 记录两张图片的图像指纹的汉明距离，计算图片相似度

<br><br>

待续……


<br>

Use the related libraries:
>
> PIL
>
> matplotlib
>
> numpy
