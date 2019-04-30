import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import load_mongodb
from utils import data_trans

matplotlib.use('TkAgg')


def color_gradient(steps, gradient):
    color_start = [0, 0, 255]
    color = [int(color_start[i] + steps * gradient[i]) for i in range(3)]
    color_hex = '#'
    for i in range(3):
        h = str(hex(color[i]))[2:]
        if len(h) == 1:
            h = '0' + h
        color_hex += h
    return color_hex


def draw(verify_paths):
    n = len(verify_paths)
    data = np.zeros((n, 128, 128, 3))
    for i, raw_data in enumerate(verify_paths):
        points = data_trans.analysis_data(raw_data)
        points = data_trans.scale(points)
        points = data_trans.get_velocity(points)
        for point in points:
            data[i][point['x']][point['y']] = [1, point['time'] / 100, point['v']]

    color_start = (0, 0, 255)
    color_end = (255, 0, 0)
    all_gradient = [color_end[i] - color_start[i] for i in range(3)]
    plt.figure()
    for i in range(n):
        v_max = -1
        for x in range(128):
            for y in range(128):
                if data[i][x][y][-1] > v_max:
                    v_max = data[i][x][y][-1]
        gradient = [g / v_max for g in all_gradient]
        plt.subplot(3, 3, i + 1)
        plt.title('max_v:' + str(v_max)[:4])
        for x in range(128):
            for y in range(128):
                if data[i][x][y][0] == 0:
                    continue
                else:
                    steps = data[i][x][y][2]
                    c = color_gradient(steps, gradient)
                    plt.scatter(x, y, c=c)
    plt.show()


def draw_matrix(data):
    color_start = (0, 0, 255)
    color_end = (255, 0, 0)
    all_gradient = [color_end[i] - color_start[i] for i in range(3)]
    v_max = data[:, :, 2].max()
    fig = plt.figure()
    for x in range(128):
        for y in range(128):
            if data[x][y][-1] > v_max:
                v_max = data[x][y][-1]

    gradient = [g / v_max for g in all_gradient]
    plt.title('max_v:' + str(v_max)[:4])
    for x in range(128):
        for y in range(128):
            if data[x][y][0] == 0:
                continue
            else:
                steps = data[x][y][2]
                c = color_gradient(steps, gradient)
                plt.scatter(x, y, c=c)
    return fig


if __name__ == '__main__':
    mongo_data = load_mongodb.MongoData()
    # verify_paths = mongo_data.get_mongodb_batch()
    # draw(verify_paths)
    ms = mongo_data.get_batch_matrix()
    fig = draw_matrix(ms)
    plt.show(fig)
