#coding:utf-8
#在图像上画园
import cv2 as cv
import numpy as np
#鼠标连接的函数：画一个园
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),8,(255,0,0),-1)
#创建一个黑色画布
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('image')
#添加鼠标点击事件
cv.setMouseCallback('image',draw_circle)

while True:
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
