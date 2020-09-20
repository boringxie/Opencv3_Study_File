#coding:utf-8
#通过cv.getTickCount()测量代码运行事件


import cv2 as cv
import  numpy as np
cv.setUseOptimized(True)
print(cv.useOptimized())
img1 = cv.imread('D:\python_file\Opencv3_study_file\images\money.jpg')

e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2-e1)/cv.getTickFrequency()
print(t)


#最后得到0.1807574秒