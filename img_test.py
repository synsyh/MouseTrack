import random
import time

import numpy as np
import cv2


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), 2, (255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 2, (255), -1)


drawing = False
ix, iy = -1, -1
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
img = np.zeros((255, 255, 1), np.uint8)
track_data = np.zeros((100, 255, 255, 1))
# cv2.imshow('image', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
i = 0
while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 32:
        i += 1
        track_data[i] = img
        img = np.zeros((255, 255, 1), np.uint8)
    elif k == 27 or i == 99:
        time_now = time.time()
        rand = str(random.random())[2:7]
        np.save('mouse_track' + rand, track_data)
        break
cv2.destroyAllWindows()
