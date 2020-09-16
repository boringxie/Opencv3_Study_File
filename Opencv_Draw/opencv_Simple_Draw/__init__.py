#coding:utf-8
#画笔工具

import cv2 as cv
import numpy as np

#创建图像
img = np.zeros((512,512,3),np.uint8)
#绘制线
cv.line(img,(0,0),(511,511),(255,0,0),5)
#绘制矩形
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
#绘制园
cv.circle(img,(447,63),63,(0,0,255),-1)
#绘制椭圆
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#绘制多边形
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
#向图像添加文本
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

while True:
    cv.imshow('frame',img)
    #读取键盘:按下q键结束程序
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()