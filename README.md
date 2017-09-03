# Identify similar images

- 利用直方图距离计算图片相似度

计算公式：

<img src="http://chart.googleapis.com/chart?cht=tx&chl=Sim(G,S)=\frac{1}{N}\sum_{i=1}^{N}{(1-\frac{|g_i-s_i|}{Max(g_i,s_i)})}" style="border:none;">

其中，G和S为两张图片的图像颜色分布直方图，N为颜色空间样点数。

这里使用分块的方法计算相似度，用以提高各部分的特征，防止图片颜色相似导致计算的相似度高。

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
