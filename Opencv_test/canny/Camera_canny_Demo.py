#coding:utf-8
#实时边缘检测
#导入opencv-python
import cv2
#导入科学计算库numpy
import numpy as np

#获取摄像头，传入0表示获取系统默认摄像头
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#打开cap
cap.open(0)

#循环
while cap.isOpened():
    #获取画面
    flag,frame = cap.read()
    if not flag:
        break
    #进行canny边缘检测
    frame = cv2.Canny(frame,50,100)
    #将单通道图像复制3份，摞成三通道图像
    frame = np.dstack((frame,frame,frame))
    cv2.imshow('my_window',frame)
    #获取键盘上按下的那个按键
    key_pressed = cv2.waitKey(60)
    print('键盘被按下的按键是:',key_pressed)
    if key_pressed == 27:
        break

cap.release()
cv2.destroyAllWindows()