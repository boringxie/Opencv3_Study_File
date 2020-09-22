#coding:utf-8
#图像混合


import cv2 as cv
import numpy as np,sys

A = cv.imread('D:/python_file/Opencv3_study_file/images/A.jpg')
B = cv.imread('D:/python_file/Opencv3_study_file/images/money.jpg')



# 给A生成高斯金字塔
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)
# 给B生成高斯金字塔
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)
# A生成金字塔图像
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)
# B生成金字塔图像
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)
# 在每一层为图像添加左右两个部分
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))
    LS.append(ls)
# 现在重建
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])
# 两个图像的一半连接
real = np.hstack((A[:,:int(cols/2)],B[:,int(cols/2):]))
cv.imshow('ls_',ls_)
cv.imshow('real',real)
cv.imwrite('D:/python_file/Opencv3_study_file/images/Pyramid_blending2.jpg',ls_)
cv.imwrite('D:/python_file/Opencv3_study_file/images/Direct_blending.jpg',real)
cv.waitKey(0)
cv.destroyAllWindows()