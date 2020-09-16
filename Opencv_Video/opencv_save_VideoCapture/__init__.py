#coding:utf-8
#保存处理后的视频
#从摄像头捕捉图像，将图像一帧一帧存储起来
import cv2 as cv
import numpy as np

#打开指定摄像头
cap = cv.VideoCapture(0)

#创建视频实例和定义视频格式
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))


while cap.isOpened():
    #捕获图像到frame
    ret,frame = cap.read()

    #如果读取没有读取到图像结束循环
    if not ret:
        print("没有捕获到图像，退出程序")
        break
    #输出图像翻转
    frame = cv.flip(frame,0)

    #将处理好的图像写入out实例
    out.write(frame)

    cv.imshow('frame',frame)
    #读取键盘:按下q键结束程序
    if cv.waitKey(1) == ord('q'):
        break

#完成内容 释放捕获的图像
cap.release()
out.release()
#关闭所有窗口
cv.destroyAllWindows()