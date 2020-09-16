#coding:utf-8
#基础的图像操作
import numpy as np
import cv2 as cv

#访问和修改像素值
img = cv.imread('D:\python_file\Opencv3_study_file\images\!face.png')
'''
>>> px = img[100,100]
>>> print( px )

[157 166 200]

# 只访问蓝色像素
>>> blue = img[100,100,0]
>>> print( blue )

157

 可以用同样的方式修改像素值
>>> img[100,100] = [255,255,255]
>>> print( img[100,100] )


[255 255 255]
157
'''
#访问图像属性
'''
shape:形状
>>> print( img.shape )
(342, 548, 3)
size:图像大小
>>> print( img.size )
562248
type:字节格式
>>> print( img.dtype )
uint8
'''
#图像投资回报率
'''
>>> ball = img[280:340, 330:390]
>>> img[273:333, 100:160] = ball
'''
#拆分和合并图像通道
'''
#拆分和合并
>>> b,g,r = cv.split(img)
>>> img = cv.merge((b,g,r))
'''
#为图像创建边框（填充）