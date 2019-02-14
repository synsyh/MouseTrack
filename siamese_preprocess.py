import linecache
import math

import check_data
import data_trans
import numpy as np
import random


def get_velocity(ps):
    for i in range(len(ps) - 2):
        ps[i + 1]['v'] = math.sqrt((ps[i + 2]['x'] - ps[i]['x']) ** 2 + (ps[i + 2]['y'] - ps[i]['y']) ** 2) / (
                ps[i + 2]['time'] - ps[i]['time'])
    ps[0]['v'] = 0
    ps[-1]['v'] = ps[-2]['v']
    return ps


def tmp():
    file_paths = ['./data/siamese/sun2', './data/siamese/yuan2', './data/siamese/yu2']
    x_ratio, y_ratio = check_data.get_scale_ratio(file_paths)
    data = np.zeros((9000, 2, 128, 128, 3))

    for n, file_path in enumerate(file_paths):
        with open(file_path, 'r') as f:
            for i, line in enumerate(f.readlines()):
                points = data_trans.analysis_data(line)
                points = sorted(points, key=lambda x: x['time'])
                points = get_velocity(points)
                for point in points:
                    data[i * 10 + j + 3000 * n][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1,
                                                                                                         point['time'],
                                                                                                         point['v']]


def get_batch():
    x_ratio = 0.27367970921530893
    y_ratio = 0.2158152082279548
    k = random.sample(range(50000), 32)
    data = [np.zeros((32, 128, 128, 3)) for i in range(2)]
    label = np.zeros((32,))

    for iter, i in enumerate(k):
        if i < 25000:
            line = linecache.getline('./data/siamese_data/siamese0_shuffle.txt', i+1)
            label[iter] = 0
        else:
            i -= 25000
            line = linecache.getline('./data/siamese_data/siamese1_shuffle.txt', i+1)
            label[iter] = 1
        points1 = data_trans.analysis_data(line.split(' ')[0])
        points2 = data_trans.analysis_data(line.split(' ')[1])
        points1 = get_velocity(points1)
        points2 = get_velocity(points2)
        for point in points1:
            data[0][iter][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
        for point in points2:
            data[1][iter][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    return data, label


def get_eval_batch():
    x_ratio = 0.27367970921530893
    y_ratio = 0.2158152082279548
    k = random.sample(range(5000), 20)
    data = [np.zeros((20, 128, 128, 3)) for i in range(2)]
    label = np.zeros((20,))
    true_num = random.choice(range(20))
    label[true_num] = 1
    true_category = random.randint(5000, 10000)
    true_line = linecache.getline('./data/siamese_data/siamese_shuffle_eval', true_category)
    true_points1 = data_trans.analysis_data(true_line.split(' ')[0])
    true_points2 = data_trans.analysis_data(true_line.split(' ')[1])
    true_points1 = get_velocity(true_points1)
    true_points2 = get_velocity(true_points2)
    for point in true_points1:
        data[0][true_num][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    for point in true_points2:
        data[1][true_num][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    data[0] = data[0][true_num] * 20
    for iter, i in enumerate(k):
        if iter == true_num:
            continue
        line = linecache.getline('./data/siamese_data/siamese_shuffle_eval', i+1)
        points1 = data_trans.analysis_data(line.split(' ')[0])
        points2 = data_trans.analysis_data(line.split(' ')[1])
        points1 = get_velocity(points1)
        points2 = get_velocity(points2)
        for point in points1:
            data[0][iter][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
        for point in points2:
            data[1][iter][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]

    return data, label
