import cv2 as cv
img=cv.imread("E:\\P.png") #读取指定位置的一副图片
cv.namedWindow("Image") #初始化一个名为Image的窗口
cv.imshow("Image",img) # 显示图片
cv.waitKey(0) #等待键盘触发事件，释放窗口
