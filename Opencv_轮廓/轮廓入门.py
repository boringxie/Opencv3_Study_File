#coding:utf-8
#轮廓入门

import numpy as np
import cv2 as cv

img = cv.imread('D:/python_file/Opencv3_study_file/images/Strat.png')

imgary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(imgary,127,255,0)
#cv.CHAIN_APPROX_NONE  找到所有边脚 |cv.CHAIN_APPROX_SIMPLE 节省内存找到框框的边脚
contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv.moments(cnt)

epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)

print(approx)
cv.drawContours(img,approx, -1, (0,255,255), 3)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()

