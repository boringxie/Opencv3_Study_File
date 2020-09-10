#coding:utf-8
#实时边缘检测
#导入opencv-python
import cv2
#导入科学计算库numpy
import numpy as np

#导入人脸检测器、眼睛检测器、微笑检测器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
#获取摄像头，传入0表示获取系统默认摄像头
cap = cv2.VideoCapture(0)
#循环
while cap.isOpened():
    #获取画面
    ret,frame = cap.read()
    faces = face_cascade.detectMultiScale(frame,1.3,2)
    img =frame
    for (x,y,w,h) in faces:
        #画出人脸框，蓝色，画笔宽度微
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #框选出人脸区域，在人脸区域进行人眼检测，节省计算资源
        face_area = img[y:y+h,x:x+w]
        ##人眼检测
        #用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        eyes = eye_cascade.detectMultiScale(face_area,1.3,10)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0, 255, 0),1)
        ##微笑检测
        #用微笑级联分类器引擎在人脸区域进行人眼识别，返回的eyes为嘴巴坐标列表
        smiles = smile_cascade.detectMultiScale(face_area,scaleFactor=1.16,minNeighbors=65,minSize=(25,25),flags=cv2.CASCADE_SCALE_IMAGE)
        for (ex,ey,ew,eh) in smiles:
            #画出微笑框红色，线宽为1
            cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,0,255),1)
            cv2.putText(img,'Smile',(x,y-7),3,1.2,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('my_window',img)
    #获取键盘上按下的那个按键
    key_pressed = cv2.waitKey(60)
    print('键盘被按下的按键是:',key_pressed)
    if key_pressed == 27:
        break

cap.release()
cv2.destroyAllWindows()