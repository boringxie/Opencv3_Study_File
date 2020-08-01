import cv2 as cv

src = cv.imread("./!face.png")
cv.namedWindow("NO.1 image",cv.WINDOW_AUTOSIZE)
cv.imshow("NO.1 image",src)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,Python!")