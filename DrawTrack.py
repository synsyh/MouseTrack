import math
import random
import time

import cv2
import numpy as np


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, start_time, last_x, last_y, last_2_x, last_2_y, last_2_time, last_time, now_time
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        start_time = time.time()
        last_2_x = last_x = x
        last_2_y = last_y = y
        last_2_time = last_time = time.time()

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            x = max(0, x)
            x = min(x, 254)
            y = max(0, y)
            y = min(y, 254)
            img[y][x][0] = 255
            data[y][x][0] = 255
            now_time = time.time()
            data[y][x][1] = now_time - start_time
            v = math.sqrt((last_2_x - x) ** 2 + (last_2_y - y) ** 2) / (now_time - last_2_time)
            data[last_y][last_x][2] = v
            last_2_x = last_x
            last_2_y = last_y
            last_x = x
            last_y = y
            last_time = now_time
            last_2_time = last_time
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x = max(0, x)
        x = min(x, 254)
        y = max(0, y)
        y = min(y, 254)
        img[y][x][0] = 255
        data[y][x][1] = time.time() - start_time


drawing = False  # 鼠标按下后为True
ix, iy = -1, -1
img = np.zeros((255, 255, 1), np.uint8)
data = np.zeros((255, 255, 3), np.float32)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
rand = str(random.random())[2:7]
data_list = np.zeros((100, 255, 255, 3))
i = 0

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 32:
        i += 1
        data_list[i] = data
        img = np.zeros((255, 255, 1), np.uint8)
        data = np.zeros((255, 255, 3), np.float32)
    elif k == 27 or i == 99:
        np.save('data_' + rand, data_list)
        break

cv2.destroyAllWindows()
