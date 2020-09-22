#coding:utf-8
#形态梯度
''':arg
它是图像扩张和侵蚀的区别。
结果将看起来像对象的轮廓。
'''
import cv2 as cv
import numpy as np

img = cv.imread('D:/python_file/Opencv3_study_file/images/I.png')
kernel = np.ones((5,5),np.uint8)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('img',img)
cv.imshow('erosion',gradient)
cv.waitKey(0)
cv.destroyAllWindows()