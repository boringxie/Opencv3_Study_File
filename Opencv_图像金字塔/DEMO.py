#coding:utf-8
#高斯金字塔and 拉普兰金字塔

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:/python_file/Opencv3_study_file/images/Opencv.png')

higher_reso = cv.pyrUp(img)
lower_reso = cv.pyrDown(higher_reso)
higher_reso2 = cv.pyrUp(lower_reso)


cv.imshow('img',img)
cv.imshow('lower_reso',lower_reso)
cv.imshow('higher_reso',higher_reso)
cv.imshow('higher_reso2',higher_reso2)
cv.waitKey(0)
cv.destroyAllWindows()