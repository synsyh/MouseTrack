import numpy as np

tmp4 = np.load('./mouse_track_4.npy')
tmp44 = np.load('./mouse_track_44.npy')
tmp444 = np.load('./mouse_track_444.npy')
tmp4 = np.append(tmp4, tmp44, tmp444)
print('')
