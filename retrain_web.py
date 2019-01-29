# 模型再训练，固定好模型，训练全连接层 web
import keras
import data_trans
import math
import numpy as np
import check_data
import fake_data


def get_velocity(ps):
    for i in range(len(ps) - 2):
        ps[i + 1]['v'] = math.sqrt((ps[i + 2]['x'] - ps[i]['x']) ** 2 + (ps[i + 2]['y'] - ps[i]['y']) ** 2) / (
                ps[i + 2]['time'] - ps[i]['time'])
    ps[0]['v'] = 0
    ps[-1]['v'] = ps[-2]['v']
    return ps


n = 10
file_path = './data/xuhao_tmp'
model_path = './model_3PEOPLE_DRAW2_10.h5'

data = np.zeros((n, 128, 128, 3))
model = keras.models.load_model(model_path)

for layer in model.layers[:-1]:
    layer.trainable = False

x_ratio, y_ratio = check_data.get_scale_ratio(file_path)

with open(file_path) as f:
    for i, line in enumerate(f.readlines()):
        points = data_trans.analysis_data(line)
        points = sorted(points, key=lambda x: x['time'])
        for j in range(10):
            points = fake_data.create_fake(points)
            points = get_velocity(points)
            for point in points:
                data[j][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'], point['v']]

y_train = np.ones(n) * 3
y_train = keras.utils.to_categorical(y_train, 4)
model.fit(data, y_train, batch_size=1, epochs=5)

x_ratio, y_ratio = check_data.get_scale_ratio('./data/xuhao_new')
test_data = np.zeros((40, 128, 128, 3))
with open('./data/xuhao_new') as f:
    for i, line in enumerate(f.readlines()):
        points = data_trans.analysis_data(line)
        points = sorted(points, key=lambda x: x['time'])
        points = get_velocity(points)
        for point in points:
            test_data[i][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'], point['v']]
    predictions = model.predict(test_data)
    for i in range(40):
        print('num:'+str(i)+' predict to:' + str(np.argmax(predictions[i])) + ' num is:' + str(max(predictions[i])))

