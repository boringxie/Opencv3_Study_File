import cv2 as cv

src = cv.imread("D:/python_file/Opencv3_study_file/images/PT_Picture.jpg",-1)
cv.namedWindow("NO.1 image",cv.WINDOW_AUTOSIZE)
cv.imshow("NO.1 image",src)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,Python!")