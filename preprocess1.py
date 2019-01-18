import numpy as np

data = np.load('data_S.npy')
data = data[:, :, :, 0:1]
np.save('data_S_1', data)
print()
