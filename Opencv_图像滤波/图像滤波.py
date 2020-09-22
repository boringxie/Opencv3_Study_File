#coding:utf-8
#图像滤波
'''
与一维信号一样，图像也可以通过各种低通滤波器 （LPF）、高通滤波器 （HPF） 等进行滤波。LPF 有助于消除噪音、模糊图像等。HPF 滤镜有助于查找图像中的边缘。
OpenCV 提供一个函数 cv.filter2D（）来将内核与图像进行扩展。例如，我们将尝试对图像进行平均筛选器
操作的工作方式如下：将此内核保留到像素上方，将此内核下方的所有 25 个像素添加，以平均值为平均值，
并将中心像素替换为新的平均值。对于图像中的所有像素，此操作将继续。请尝试此代码并检查结果：
'''
import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread('D:/python_file/Opencv3_study_file/images/Opencv.png')
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()