import numpy as np
import keras
import cv2

data = np.load('mouse_draw_0118_1PARA_2.npz')
x_test = data['arr_2']
y_test = data['arr_3']

model = keras.models.load_model('./data/mouse_track_0118_1PARA_2.h5')

predictions = model.predict(x_test)
n = 4
print(np.argmax(predictions[n]))
print(y_test[n])
img = x_test[n]
cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()