import math
import time

import cv2
import keras

# 鼠标回调函数
import numpy as np


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

model = keras.models.load_model('./data/mouse_track_3_PARA_out.h5')
for layer in model.layers[:-1]:
    layer.trainable = False

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
        data = np.expand_dims(data, 0)
        data[:, :, :, 0] /= 255
        data[:, :, :, 1] *= 10
        data[:, :, :, 2] /= 1000
        break

cv2.destroyAllWindows()

y_train = np.array([[1.0, 0.0]])
model.fit(data, y_train,
          batch_size=1,
          epochs=10)


img = np.zeros((255, 255, 1), np.uint8)
data = np.zeros((255, 255, 3), np.float32)
while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 32:
        data = np.expand_dims(data, 0)
        data[:, :, :, 0] /= 255
        data[:, :, :, 1] *= 10
        data[:, :, :, 2] /= 1000
        break

cv2.destroyAllWindows()

predictions = model.predict(data)
print(predictions[0])



