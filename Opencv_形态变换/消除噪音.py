#coding:utf-8
#消除噪音
#开放只是侵蚀后，后扩张的另一个名字。正如我们上面所解释的，它对于消除噪音很有用
import cv2 as cv
import numpy as np

img = cv.imread('D:/python_file/Opencv3_study_file/images/Opening.png')
kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow('img',img)
cv.imshow('erosion',opening)
cv.waitKey(0)
cv.destroyAllWindows()