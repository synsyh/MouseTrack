import numpy as np

data1 = np.load('./data/data_S_1.npy')
data2 = np.load('./data/data_Y_1.npy')[:, :, :, 0:1]
data3 = np.load('./data/data_S.npy')[:, :, :, 0:1]
data4 = np.load('./data/data_Y.npy')[:, :, :, 0:1]
data = np.concatenate((data1, data3, data2, data4))

# 0 S
label1 = np.zeros(200)
# 1 Y
label2 = np.ones(200)
label = np.concatenate((label1, label2))

state = np.random.get_state()
np.random.shuffle(data)
np.random.set_state(state)
np.random.shuffle(label)
x_train = data[:300, :, :, :]
y_train = label[:300]
x_test = data[300:, :, :, :]
y_test = label[300:]

np.savez('mouse_draw_0118_1PARA_2', x_train, y_train, x_test, y_test)