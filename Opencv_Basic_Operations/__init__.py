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
''':arg
cv.BORDER_CONSTANT - 添加一个常量彩色边框。该值应作为下一个参数给出。
cv.BORDER_REFLECT - 边框将反映边框元素，像这样： fedcba_abcdefgh\hgfedcb
cv.BORDER_REFLECT_101或cv。BORDER_DEFAULT - 与上述相同，但有一个轻微的变化，像这样： gfedcb_abcdefgh\gfedcba
cv.BORDER_REPLICATE - 最后一个元素在整个过程中复制， 像这样： a _ abcdefgh _ h
cv.BORDER_WRAP - 无法解释， 它看起来像这样： cdefgh _ abcdefg
'''
''':arg
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('opencv-logo.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
'''
