# 对web采集的数据进行处理
import numpy as np
import math
import data_trans
import fake_data
import check_data


def get_velocity(ps):
    for i in range(len(ps) - 2):
        ps[i + 1]['v'] = math.sqrt((ps[i + 2]['x'] - ps[i]['x']) ** 2 + (ps[i + 2]['y'] - ps[i]['y']) ** 2) / (
                ps[i + 2]['time'] - ps[i]['time'])
    ps[0]['v'] = 0
    ps[-1]['v'] = ps[-2]['v']
    return ps


if __name__ == '__main__':
    data = np.zeros((9000, 128, 128, 3))
    file_paths = ['./data/sun2', './data/yuan2', './data/yu2']
    x_ratio, y_ratio = check_data.get_scale_ratio(file_paths)

    for n, file_path in enumerate(file_paths):
        with open(file_path, 'r') as f:
            for i, line in enumerate(f.readlines()):
                points = data_trans.analysis_data(line)
                points = sorted(points, key=lambda x: x['time'])
                for j in range(10):
                    points = fake_data.create_fake(points)
                    points = get_velocity(points)
                    for point in points:
                        data[i * 10 + j + 3000 * n][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point[
                            'time'], point['v']]
    # 1 sun
    label1 = np.zeros(3000)
    # 2 yuan
    label2 = np.ones(3000)
    # 3 yu
    label3 = np.ones(3000) * 2

    label = np.concatenate((label1, label2, label3))

    state = np.random.get_state()
    np.random.shuffle(data)
    np.random.set_state(state)
    np.random.shuffle(label)
    x_train = data[:6000, :, :, :]
    y_train = label[:6000]
    x_test = data[6000:, :, :, :]
    y_test = label[6000:]

    np.savez('track_3PEOPLE_DRAW2_10', x_train, y_train, x_test, y_test)
