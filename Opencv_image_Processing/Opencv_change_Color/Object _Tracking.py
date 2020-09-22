#coding:utf-8
#对象追踪图像版本
import cv2 as cv
import numpy as np

img = cv.imread("D:/python_file/Opencv3_study_file/images/blue.jpg")


hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#define range of blue color in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

#
mask = cv.inRange(hsv,lower_blue,upper_blue)

res = cv.bitwise_and(img,img,mask = mask)

cv.imshow('frame', img)
cv.imshow('mask', mask)
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()