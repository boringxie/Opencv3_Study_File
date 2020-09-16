#coding:utf-8
#处理捕获图像:
#从摄像头捕捉图像，将图像转换为灰度
import cv2 as cv

import numpy as np

#打开指定摄像头
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("没有打开摄像头")
    exit()
while True:
    #捕获图像到frame
    ret,frame = cap.read()

    #如果读取没有读取到图像结束循环
    if not ret:
        print("没有捕获到图像")
        break
    #输出图像设置为灰度图形
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #显示处理后的图形
    cv.imshow('frame',gray)
    #读取键盘
    if cv.waitKey(1) == ord('q'):
        break

#完成内容 释放捕获的图像
cap.release()
#关闭所有窗口
cv.destroyAllWindows()