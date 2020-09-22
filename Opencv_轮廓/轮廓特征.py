#coding:utf-8
#轮廓特征

import numpy as np
import cv2 as cv

img = cv.imread('D:/python_file/Opencv3_study_file/images/Strat.png',0)
#图片二值化
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv.moments(cnt)
#轮廓的中心点
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx,cy)

#轮廓的面积
area = cv.contourArea(cnt)
print(M['m00'])

#轮廓的框选
#计算周长
epsilon = 0.1*cv.arcLength(cnt,True)
#框选
approx = cv.approxPolyDP(cnt,epsilon,True)