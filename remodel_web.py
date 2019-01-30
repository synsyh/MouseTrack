import keras
import numpy as np

from check_data import get_scale_ratio
from data_trans import analysis_data
from fake_data import create_fake
from preprocess_web import get_velocity


def validation(file_path):
    x_ratio, y_ratio = get_scale_ratio(file_path)
    test_data = np.zeros((40, 128, 128, 3))
    with open(file_path) as f:
        for i, line in enumerate(f.readlines()):
            points = analysis_data(line)
            points = sorted(points, key=lambda x: x['time'])
            points = get_velocity(points)
            for point in points:
                test_data[i][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'], point['v']]
        predictions = model.predict(test_data)
        for i in range(40):
            print('num:' + str(i) + ' predict to:' + str(np.argmax(predictions[i])) + ' num is:' + str(
                max(predictions[i])))


model = keras.models.load_model('./model_3PEOPLE_DRAW2_10.h5')

for layer in model.layers[:-1]:
    layer.trainable = False

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(lr=0.1),
              metrics=['accuracy'])

data = np.zeros((1, 128, 128, 3))
x_ratio, y_ratio = get_scale_ratio('./data/xuhao_tmp')
with open('./data/xuhao_tmp') as f:
    for i, line in enumerate(f.readlines()):
        points = analysis_data(line)
        points = sorted(points, key=lambda x: x['time'])
        for j in range(10):
            points = create_fake(points)
            points = get_velocity(points)
            for point in points:
                data[j][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'], point['v']]
y_train = np.ones(10) * 3
y_train = keras.utils.to_categorical(y_train, 4)
model.fit(data, y_train, batch_size=1, epochs=5)

validation('./data/xuhao_new')
