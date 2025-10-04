#再写考核内容   熟悉了前面的读写内容  并更新了 1.按位与运算 2.输出坐标 的部分，对列的理解更深了
import cv2 as cv
import numpy as np

lawn1 = cv.imread("D:\computer visual\picture\sJaelOcd5Y_small.jpg",1)#读取图片
cv.imshow("lawn1",lawn1)
cv.waitKey(0)      

lawn2=cv.cvtColor(lawn1,cv.COLOR_BGR2HSV)    #转格式

low_green=np.array([35,40,40])
high_green=np.array([85,255,255])   #选中绿色范围

mask=cv.inRange(lawn2,low_green,high_green)  #制作掩模

img=cv.add(lawn1,0,mask=mask)  #与运算得出成品
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()

a = np.where(mask==255)  #找出掩模中值为255的点
for x in a[0]:
    for y in a[1]:
         print(f"绿色的坐标为：({x},{y})")  #打印坐标

