# 使用模型来预测，3个参数，2分类
import math
import time

import keras
import numpy as np
import cv2

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

model = keras.models.load_model('./data/mouse_track_3_PARA_1.h5')

img = np.zeros((255, 255, 1), np.uint8)
data = np.zeros((255, 255, 3), np.float32)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

drawing = False  # 鼠标按下后为True
ix, iy = -1, -1

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 32:
        img = img.astype('float32')
        data = np.expand_dims(data, 0)
        data[:, :, :, 0] /= 255
        data[:, :, :, 1] *= 10
        data[:, :, :, 2] /= 1000
        predictions = model.predict(data)
        print(np.argmax(predictions[0]))
        img = np.zeros((255, 255, 1), np.uint8)
        data = np.zeros((255, 255, 3), np.float32)
    elif k == 27:
        break

cv2.destroyAllWindows()

