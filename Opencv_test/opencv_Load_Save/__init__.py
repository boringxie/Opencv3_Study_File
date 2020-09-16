#coding:utf-8
import cv2 as cv
import  numpy as np

def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow('video',frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


src = cv.imread("D:\python_file\Opencv3_study_file\images\!face.png")
cv.namedWindow("NO.1 image",cv.WINDOW_AUTOSIZE)
cv.imshow("NO.1 image",src)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
#注意千万不要选择中文目录，否则无法保存
cv.imwrite("D:/images/face_gray.png",gray)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,Python!")