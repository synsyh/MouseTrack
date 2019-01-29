import keras
import numpy as np

import data_trans
from fake_data import get_velocity

data = np.zeros((1, 255, 255, 3))
x_ratio = 255/420
y_ratio = 255/530

model = keras.models.load_model('./data/model_3PEOPLE_DRAW2.h5')

with open('./data/tmp_yu') as f:
    for i, line in enumerate(f.readlines()):
        points = data_trans.analysis_data(line)
        points = sorted(points, key=lambda x: x['time'])
        points = get_velocity(points)
        for point in points:
            data[0][int(point['x']*x_ratio)][int(point['y']*y_ratio)] = [1, point['time'], point['v']]
        predictions = model.predict(data)
        print(max(predictions[0]))
        print(np.argmax(predictions[0]))

