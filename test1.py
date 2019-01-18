import numpy as np

data = np.load('DATA.npz')
img = data['arr_0']
label = data['arr_1']
x_train = img[:500, :, :, :]
y_train = label[:500]
x_test = img[500:, :, :, :]
y_test = label[500:]
x_train /= 255
np.savez('mouse_track', x_train, y_train, x_test, y_test)
print()
