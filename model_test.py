# use model to predict
import keras
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

data = np.load('mouse_track.npz')
model = keras.models.load_model('mouse_track.h5')
x_test = data['arr_2']
y_test = data['arr_3']

img = np.zeros((255, 255, 1), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

drawing = False  # 鼠标按下后为True
ix, iy = -1, -1

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 32:
        img = np.expand_dims(img, 0)
        predictions = model.predict(img)
        print(predictions[0])
        img = np.zeros((255, 255, 1), np.uint8)
    elif k == 27:
        break

cv2.destroyAllWindows()

