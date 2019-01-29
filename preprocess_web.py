# 对web采集的数据进行处理
import numpy as np
import math
import data_trans
import check_data


def get_velocity(ps):
    for i in range(len(ps) - 2):
        ps[i + 1]['v'] = math.sqrt((ps[i + 2]['x'] - ps[i]['x']) ** 2 + (ps[i + 2]['y'] - ps[i]['y']) ** 2) / (
                ps[i + 2]['time'] - ps[i]['time'])
    ps[0]['v'] = 0
    ps[-1]['v'] = ps[-2]['v']
    return ps


if __name__ == '__main__':
    data = np.zeros((900, 255, 255, 3))
    x_ratio = 255/420
    y_ratio = 255/530
    with open('./data/sun2', 'r') as f:
        for i, line in enumerate(f.readlines()):
            points = data_trans.analysis_data(line)
            points = sorted(points, key=lambda x: x['time'])
            points = get_velocity(points)
            for point in points:
                data[i][int(point['x']*x_ratio)][int(point['y']*y_ratio)] = [1, point['time'], point['v']]
    with open('./data/yuan2', 'r') as f:
        for i, line in enumerate(f.readlines()):
            points = data_trans.analysis_data(line)
            points = sorted(points, key=lambda x: x['time'])
            points = get_velocity(points)
            for point in points:
                data[i + 300][int(point['x']*x_ratio)][int(point['y']*y_ratio)] = [1, point['time'], point['v']]
    with open('./data/yu2', 'r') as f:
        for i, line in enumerate(f.readlines()):
            points = data_trans.analysis_data(line)
            points = sorted(points, key=lambda x: x['time'])
            points = get_velocity(points)
            for point in points:
                data[i + 600][int(point['x']*x_ratio)][int(point['y']*y_ratio)] = [1, point['time'], point['v']]
    # 1 sun
    label1 = np.zeros(300)
    # 2 yuan
    label2 = np.ones(300)
    # 3 yu
    label3 = np.ones(300) * 2

    label = np.concatenate((label1, label2, label3))

    state = np.random.get_state()
    np.random.shuffle(data)
    np.random.set_state(state)
    np.random.shuffle(label)
    x_train = data[:600, :, :, :]
    y_train = label[:600]
    x_test = data[600:, :, :, :]
    y_test = label[600:]

    np.savez('track_3PEOPLE_DRAW2', x_train, y_train, x_test, y_test)
