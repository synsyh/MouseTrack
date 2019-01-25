import cv2
import numpy as np

img = cv2.imread("./data/test.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色转化为灰度
gray = np.float32(gray)  # 转化为32浮点型
dst = cv2.cornerHarris(gray, 15, 23, 0.04)
# 第三个参数：Sobel算法中孔，行列变化检测边缘。3-31之间奇数
# 角点检测的敏感度
# 第二个参数：参数值越小，标记角点的记号越小

img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.namedWindow("corners", cv2.WINDOW_NORMAL)
while (True):
    cv2.imshow('corners', img)
    if cv2.waitKey(10000) & 0xff == ord('q'):  # 退出循环条件
        break
cv2.destroyAllWindows()
# cv2.imshow('corners',img)
# cv2.waitKey(0) #退出循环条件
# cv2.destroyAllWindows()