# Identify similar images

- 利用直方图距离计算图片相似度


计算公式：
<img src="http://chart.googleapis.com/chart?cht=tx&chl=Sim(G,S)=\frac{1}{N}\sum_{i=1}^{N}{(1-\frac{|g_i-s_i|}{Max(g_i,s_i)})}" style="border:none;">

其中，G和S为两张图片的图像颜色分布直方图，N为颜色空间样点数。


待续……



> Use the related libraries:
>
> PIL
>
> matplotlib
>
> numpy
