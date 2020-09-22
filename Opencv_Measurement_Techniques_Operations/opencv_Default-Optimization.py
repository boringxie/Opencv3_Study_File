#coding:utf-8
#通过cv.getTickCount()测量代码运行事件


import cv2 as cv
import  numpy as np
img = cv.imread('D:\python_file\Opencv3_study_file\images\!face.png')

print(cv.useOptimized())

e1 = cv.getTickCount()
res = cv.medianBlur(img,49)
e2 = cv.getTickCount()
t = (e2-e1)/cv.getTickFrequency()
print()


cv.setUseOptimized(False)
cv.useOptimized()

e1 = cv.getTickCount()
res = cv.medianBlur(img,49)
e2 = cv.getTickCount()
t = (e2-e1)/cv.getTickFrequency()
print()