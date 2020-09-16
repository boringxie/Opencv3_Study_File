#coding:utf-8
import cv2 as cv
import  numpy as np

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    '''
    #三通道图像
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,0] = np.ones([400,400])*255
    #img[:,:,1] = np.ones([400, 400])*255
    #img[:,:,2] = np.ones([400, 400])*255
    '''

    '''
    img = np.zeros([400,400,1],np.uint8)
    img[:,:,0] = np.ones([400,400])*127
    cv.imshow("create_iamge", img)
    '''
    #创建图像
    m1 = np.ones([3,3],np.uint8)
    #填充数据
    m1.fill(122)
    print(m1)

    #将二维数组转换成一维数组
    m2 = m1.reshape([1,9])
    print(m2)
print("-----Hi,Python!------")
src = cv.imread("D:/python_file/Opencv3_study_file/images/!face.png")
cv.namedWindow("NO.1 image",cv.WINDOW_AUTOSIZE)
cv.imshow("NO.1 image",src)
#获取运行前时间
t1 = cv.getTickCount()
#access_pixels(src)
#获取运行后时间
t2 = cv.getTickCount()
#运行总共时间
t3=(t2-t1)/cv.getTickFrequency()*1000
print(f"time:{t3}")
cv.waitKey(0)
cv.destroyAllWindows()