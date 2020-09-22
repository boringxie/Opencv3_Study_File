#coding:utf-8
#图形的缩放

import cv2 as cv
import numpy as np

img = cv.imread("D:/python_file/Opencv3_study_file/images/!face.png")

height,width = img.shape[:2]

res1 = cv.resize(img, (int(width/2), int(height/2)), interpolation=cv.INTER_CUBIC)
res2 = cv.resize(img,(2*width,2*height),interpolation = cv.INTER_CUBIC)

cv.imshow('img',res1)
cv.imshow('img2',res2)

cv.waitKey(0)
cv.destroyAllWindows()

