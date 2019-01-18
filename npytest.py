import numpy as np

tmp4 = np.load('./mouse_track_4.npy')
tmp44 = np.load('./mouse_track_44.npy')
tmp444 = np.load('./mouse_track_444.npy')
tmp4 = np.concatenate((tmp4, tmp44, tmp444))

label4 = np.zeros(300)

tmp6 = np.concatenate(
    (np.load('./mouse_track_6.npy'), np.load('./mouse_track_66.npy'), np.load('./mouse_track666.npy')))
label6 = np.ones(300)
data = np.concatenate((tmp4, tmp6))
label = np.concatenate((label4, label6))
state = np.random.get_state()
np.random.shuffle(data)
np.random.set_state(state)
np.random.shuffle(label)
np.savez('data', data, label)
print('')
