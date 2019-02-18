# 使用模型来预测，使用绘制数据而不是临时绘制，3参数3分类
import keras
import numpy as np

import check_data
import data_trans
from preprocess_web import get_velocity

data = np.zeros((60, 128, 128, 3))
x_ratio, y_ratio = check_data.get_scale_ratio('./data/test_data')

model = keras.models.load_model('model_3PEOPLE_DRAW2_10.h5')

with open('./data/test_data') as f:
    for i, line in enumerate(f.readlines()):
        points = data_trans.analysis_data(line)
        points = sorted(points, key=lambda x: x['time'])
        points = get_velocity(points)
        for point in points:
            data[i][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'], point['v']]
    predictions = model.predict(data)
    for i in range(60):
        print('NO.' + str(i) + ' predict to:' + str(np.argmax(predictions[i])) + ' num is:' + str(predictions[i]))
