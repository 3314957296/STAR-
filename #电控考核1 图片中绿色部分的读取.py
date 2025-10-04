#电控考核1  图片中绿色部分的读取
import cv2 as cv
import numpy as np      

# 读取图像
fengjing1 = cv.imread("D:/computer visual/picture/sJaelOcd5Y_small.jpg",cv.IMREAD_REDUCED_COLOR_2)
# 转换为HSV颜色空间
fengjing2 = cv.cvtColor(fengjing1,cv.COLOR_BGR2HSV)
# 定义绿色的HSV范围
lower_green = np.array([35,40,40])
higher_green =np.array([77,255,255])
# 创建掩膜
mask=cv.inRange(fengjing2,lower_green,higher_green) 
# 提取绿色部分
result=cv.bitwise_and(fengjing1,fengjing1,mask=mask)
# 显示结果
x_coords,y_coords =  np.where(mask!=0)
for x,y in zip(x_coords,y_coords):
    print("绿色的坐标为：({x},{y})".format(x=x,y=y))
cv.imshow("result",result)
cv.waitKey(0)
cv.destroyAllWindows()
