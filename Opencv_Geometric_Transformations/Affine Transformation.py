#coding:utf-8
#仿射变换
#在仿射变换中，原始图像中的所有平行线仍将在输出图像中平行。为了找到变换矩阵，
# 我们需要输入图像及其在输出图像中的相应位置中的三个点。然后cv.getAffineTransform将创建一个2x3矩阵，这是要传递给cv.warpAffine。
import cv2 as cv
import numpy as np

img = cv.imread('D:/python_file/Opencv3_study_file/images/!face.png')
rows,cols,ch = img.shape
#旋转前的点
pts1 = np.float32([[50,50],[200,50],[50,200]])
#旋转后的点
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))



cv.imshow('OUTPUT',dst)
cv.waitKey(0)
cv.destroyAllWindows()