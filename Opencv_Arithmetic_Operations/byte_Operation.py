#coding:utf-8
#图像的复合运算
#学习图像上的多个算术运算，如加法、减法、位位运算等。
#了解这些功能：cv.add（）、cv.addWeighted（）等。
#图像混合
import cv2 as cv
import numpy as np

img1 = cv.imread('D:\python_file\Opencv3_study_file\images\!face.png')
img2 = cv.imread('D:\python_file\Opencv3_study_file\images\A.jpg')
#我想将图片1放在图片2的左上角 所以创建roi
rows,cols,channels = img2.shape
rows=rows+250
cols=cols+250
roi = img1[250:rows, 250:cols]

img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

img2_fg = cv.bitwise_and(img2,img2,mask = mask)

dst = cv.add(img1_bg,img2_fg)
img1[250:rows, 250:cols] = dst

cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
