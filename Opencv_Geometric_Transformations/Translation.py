#coding:utf-8
#图形的偏移

import numpy as np
import cv2 as cv

img = cv.imread("D:/python_file/Opencv3_study_file/images/!face.png",0)
rows,cols = img.shape

#通过float32([[1,0,x],[0,1,y]])，通过x,y修改偏移量
M = np.float32([[1,0,50],[0,1,100]])
#warpAffine(图像实例,图像偏移值,图像长宽)
dst = cv.warpAffine(img,M,(cols-50,rows-50))

cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
