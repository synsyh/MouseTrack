import numpy as np

data = np.concatenate(
    (np.load('./data/data_S.npy'), np.load('./data/data_Y.npy')))
label1 = np.zeros(100)
label2 = np.ones(100)
label = np.concatenate((label1, label2))
state = np.random.get_state()
np.random.shuffle(data)
np.random.set_state(state)
np.random.shuffle(label)
x_train = data[:150, :, :, :]
y_train = label[:150]
x_test = data[150:, :, :, :]
y_test = label[150:]
x_train[:, :, :, 0] /= 255
x_test[:, :, :, 0] /= 255
x_train[:, :, :, 1] *= 10
x_test[:, :, :, 1] *= 10
x_train[:, :, :, 2] /= 1000
x_test[:, :, :, 2] /= 1000
np.savez('./data/mouse_track_3_PARA_2_PEOPLE', x_train, y_train, x_test, y_test)
print()
