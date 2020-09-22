#coding:utf-8
#图形的旋转

import cv2 as cv
import numpy as np

img = cv.imread('D:/python_file/Opencv3_study_file/images/!face.png',0)
rows,cols = img.shape
#getRotationMatrix2D:图形的长宽，角度，缩放
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()