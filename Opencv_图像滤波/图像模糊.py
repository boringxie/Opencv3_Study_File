#coding:utf-8
#图像渐变


import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt
img = cv.imread('D:/python_file/Opencv3_study_file/images/Opencv.png')
#高斯模糊：blur = cv.GaussianBlur(img,(5,5),0)
#中位数模糊：median = cv.medianBlur(img,5)
#双边过滤：blur = cv.bilateralFilter(img,9,75,75)
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()