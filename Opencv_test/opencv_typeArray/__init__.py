#�����������ͼ��
#һ��BGR һ���Ҷ�
import cv2
import numpy as np
import os

randomByteArray = bytearray(os.urandom(120000))
flatNumoyArray = np.array(randomByteArray)

grayImage = flatNumoyArray.reshape(300,400)
cv2.imwrite('D:/images/RandomGray.png',grayImage)


bgrImage = flatNumoyArray.reshape(100,400,3)
cv2.imwrite('D:/images/RandomColor.png',bgrImage)