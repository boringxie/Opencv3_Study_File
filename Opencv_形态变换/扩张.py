#coding:utf-8
#扩张
''':arg
它只是与侵蚀相反。在这里，如果内核下至少有一个像素是"1"，则像素元素为"1"。因此，它增加了图像中的白色区域或前景对象的大小增加。
通常，在除噪等情况下，侵蚀后是扩张。因为，侵蚀可以消除白色噪音，但它也会缩小我们的物体。因此，我们扩张它。既然噪音消失了，它们就不会再回来了，
但我们的物体面积增加了。它还可用于连接对象的断开部分。
'''
import cv2 as cv
import numpy as np

img = cv.imread('D:/python_file/Opencv3_study_file/images/I.png')
kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(img,kernel,iterations = 1)
cv.imshow('img',img)
cv.imshow('erosion',dilation)
cv.waitKey(0)
cv.destroyAllWindows()