#coding:utf-8
#侵蚀

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:/python_file/Opencv3_study_file/images/I.png')
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)

#subplot  121 意思是1*2的图像1
plt.subplot(121),plt.imshow(img),plt.title('Original')
#xtick：在x轴上显示标签 1.坐标：[] 2.标签内容：[]  3.标签旋转角度rotation=？
#yticks：在x轴上显示标签 1.坐标：[] 2.标签内容：[]  3.标签旋转角度rotation=？
plt.xticks([]), plt.yticks([])
#subplot  122 意思是1*2的图像2
plt.subplot(122),plt.imshow(erosion),plt.title('erosion')
#xtick：在x轴上显示标签 1.坐标：[] 2.标签内容：[]  3.标签旋转角度rotation=？
#yticks：在x轴上显示标签 1.坐标：[] 2.标签内容：[]  3.标签旋转角度rotation=？
plt.xticks([100,0],['OK'],rotation=90),plt.yticks([100,0],['OK'],rotation=0)
plt.show()
