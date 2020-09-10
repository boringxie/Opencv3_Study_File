#coding:utf-8
#调用摄像头画面
#导入opencv-python
import cv2

#获取摄像头，传入0表示获取系统默认摄像头
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#打开cap
cap.open(0)

#循环
while cap.isOpened():
    #获取画面
    flag,frame = cap.read()
    
    cv2.imshow('my_window',frame)
    
    #获取键盘上按下的那个按键
    key_pressed = cv2.waitKey(60)
    print('键盘被按下的按键是:',key_pressed)
    if key_pressed == 27:
        break

cap.release()
cv2.destroyAllWindows()