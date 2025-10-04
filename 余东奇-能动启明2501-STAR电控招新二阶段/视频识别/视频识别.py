import cv2 as cv
import numpy as np

#读取视频
video = cv.VideoCapture("D:/computer visual/picture/sucai.mp4")

#获取视频的宽高
width =int (video.get(cv.CAP_PROP_FRAME_WIDTH))
height =int (video.get(cv.CAP_PROP_FRAME_HEIGHT))

#获取视频的帧率
fps = video.get(cv.CAP_PROP_FPS)

#界定绿色范围
low_green = np.array([35,50,50])
high_green = np.array([70,255,255]) 

#创建输出的视频格式
fourcc = cv.VideoWriter_fourcc(*"mp4v")
#给出输出路径
out_pass ="D:/computer visual/picture/sucai_only_green.mp4"

#搭建视屏框架
out = cv.VideoWriter(  #VideoWriter需要整数类型,一定注意别又错了
	out_pass ,#输出路径
    fourcc,
	fps,
	(width,height))

#提取每一帧画面
while video.isOpened():
    ret,frame = video.read()
    if not ret:
        break

#对每一帧进行处理
    frame_green = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask = cv.inRange(frame_green,low_green,high_green)
    frame_only_green = cv.bitwise_and(frame,frame,mask=mask)
   

#合并出新视频  必须放入循环内，逐帧添加
    out.write(frame_only_green)

# 关闭原视频读取流
video.release()  
# 关闭新视频写入流
out.release()
cv.destroyAllWindows()
