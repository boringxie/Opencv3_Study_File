#coding:utf-8
#图像的复合运算
#学习图像上的多个算术运算，如加法、减法、位位运算等。
#了解这些功能：cv.add（）、cv.addWeighted（）等。
#图像混合
import cv2 as cv
import numpy as np

img1 = cv.imread('D:\python_file\Opencv3_study_file\images\A.jpg')
img2 = cv.imread('D:\python_file\Opencv3_study_file\images\money.jpg')
print(img1.shape)
print(img2.shape)
#两个图像一样的shape才能运行图像运算
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
