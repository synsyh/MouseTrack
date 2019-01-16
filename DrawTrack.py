import copy
import math
import random
import time

import cv2
import numpy as np


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), 5, (255, 255, 255), -1)
            mouse_track.append([x, y, time.time()])
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 5, (255, 255, 255), -1)
        mouse_track.append([x, y, time.time()])


drawing = False  # 鼠标按下后为True
ix, iy = -1, -1
mouse_track = []
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
time_now = time.time()
rand = str(random.random())[2:7]

with open('./MouseTrack' + rand + '.txt', 'w') as f:
    with open('./clean_data' + rand + '.txt', 'w') as w:
        while True:
            cv2.imshow('image', img)
            k = cv2.waitKey(1) & 0xFF
            if k == 32:
                img = np.zeros((512, 512, 3), np.uint8)
                if mouse_track:
                    start = copy.copy(mouse_track[0])
                    mouse_track[0][-1] = mouse_track[0][-1] - start[-1]
                    for i, n in enumerate(mouse_track[:-1]):
                        mouse_track[i + 1][-1] = mouse_track[i + 1][-1] - start[-1]
                        if i == 0:
                            v = 0
                        else:
                            dis = math.sqrt((float(mouse_track[i - 1][0]) - float(mouse_track[i + 1][0])) ** 2 + (
                                    float(mouse_track[i - 1][1]) - float(mouse_track[i + 1][1])) ** 2)
                            v = format(dis / (mouse_track[i + 1][-1] - mouse_track[i - 1][-1]), '.5f')
                        w.write('(' + str(n[0]) + ',' + str(n[1]) + ')' + ',' + str(n[-1]) + ',' + str(v) + '\n')
                    mouse_track[-1][-1] = mouse_track[-1][-1] - start[-1]
                    f.write(str(mouse_track) + '\n')
                    w.write('**************\n')
                    mouse_track = []
            elif k == 27:
                if mouse_track:
                    start = mouse_track[0]
                    for n in mouse_track:
                        n[-1] = n[-1] - start[-1]
                    f.write(str(mouse_track) + '\n')
                break

        cv2.destroyAllWindows()
