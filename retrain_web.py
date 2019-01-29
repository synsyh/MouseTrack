# 模型再训练，固定好模型，训练全连接层 web
import keras
import data_trans
import math
import numpy as np
import check_data


def get_velocity(ps):
    for i in range(len(ps) - 2):
        ps[i + 1]['v'] = math.sqrt((ps[i + 2]['x'] - ps[i]['x']) ** 2 + (ps[i + 2]['y'] - ps[i]['y']) ** 2) / (
                ps[i + 2]['time'] - ps[i]['time'])
    ps[0]['v'] = 0
    ps[-1]['v'] = ps[-2]['v']
    return ps


n = 1
file_path = ''
model_path = ''

data = np.zeros((n, 255, 255, 3))
model = keras.models.load_model(model_path)

for layer in model.layers[:-1]:
    layer.trainable = False

x_ratio, y_ratio = check_data.get_scale_ratio(file_path)

with open(file_path) as f:
    for i, line in enumerate(f.readlines()):
        points = data_trans.analysis_data(line)
        points = sorted(points, key=lambda x: x['time'])
        points = get_velocity(points)
        for point in points:
            data[i][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'], point['v']]

y_train = np.ones(300) * n

model.fit(data, y_train, batch_size=1, epochs=10)
