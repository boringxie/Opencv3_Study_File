#coding:utf-8
#收盘

import cv2 as cv
import numpy as np
#关闭是反向打开，扩张后跟侵蚀。它可用于关闭前景对象内的小孔或对象上的小黑点。
img = cv.imread('D:/python_file/Opencv3_study_file/images/closing.png')
kernel = np.ones((5,5),np.uint8)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('img',img)
cv.imshow('erosion',closing)
cv.waitKey(0)
cv.destroyAllWindows()