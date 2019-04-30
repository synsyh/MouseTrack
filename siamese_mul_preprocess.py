import linecache
import random

import numpy as np

from utils import data_trans
from siamese_preprocess import get_velocity


def load_data():
    file_list = ['./data/siamese_data/mul_sun', './data/siamese_data/mul_yu', './data/siamese_data/mul_yuan']
    all_lines = []
    n_split = 20
    for file_path in file_list:
        with open(file_path) as f:
            line_split = []
            lines = []
            for j, line in enumerate(f.readlines()):
                if j % n_split == 0:
                    lines.append(line_split)
                    line_split = []
                line_split.append(line)
            lines.append(line_split)
            lines.remove(lines[0])
            all_lines.append(lines)
    return all_lines


def create_mul1():
    all_lines = load_data()
    with open('./data/siamese_data/mul_1.txt', 'a') as w:
        for x in range(3):
            for y in range(10):
                for j1 in range(15):
                    for j2 in range(15):
                        w.write(all_lines[x][y][j1].strip() + ' ' + all_lines[x][y][j2].strip() + '\n')


def create_mul2():
    all_lines = load_data()
    with open('./data/siamese_data/mul_0.txt', 'a') as w:
        for x in range(3):
            for y in range(10):
                for j in range(15):
                    first = all_lines[x][y][j]
                    for x1 in range(3):
                        for y1 in range(10):
                            if y1 == y and x1 == x:
                                continue
                            for j1 in range(15):
                                second = all_lines[x1][y1][j1]
                                w.write(first.strip() + ' ' + second.strip() + '\n')


def get_batch():
    x_ratio = 0.3
    y_ratio = 0.2
    k = random.sample(range(202500), 32)
    data = [np.zeros((32, 128, 128, 3)) for i in range(2)]
    label = np.zeros((32,))

    for iter, i in enumerate(k):
        if i < 195750:
            line = linecache.getline('./data/siamese_data/mul_0.txt', i + 1)
            label[iter] = 0
        else:
            i -= 195750
            line = linecache.getline('./data/siamese_data/mul_1.txt', i + 1)
            label[iter] = 1
        points = data_trans.analysis_data(line.split(' '))
        points1 = get_velocity(points[0])
        points2 = get_velocity(points[1])
        for point in points1:
            data[0][iter][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
        for point in points2:
            data[1][iter][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    return data, label


def get_eval_batch():
    x_ratio = 0.3
    y_ratio = 0.2
    all_lines = load_data()
    data = [np.zeros((20, 128, 128, 3)) for i in range(2)]
    x, y, z = random.randint(0, 2), random.randint(0, 9), random.randint(15, 19)
    true_line1 = all_lines[x][y][z]

    tmp = list(range(15, 20))
    tmp.remove(y)
    z_2_t = random.choice(tmp)
    true_line2 = all_lines[x][y][z_2_t]

    tmp_data = np.zeros((1, 128, 128, 3))
    true_points1 = data_trans.analysis_data(true_line1)
    points = get_velocity(true_points1)
    for point in points:
        tmp_data[0][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100,
                                                                             point['v']]
    for n in range(20):
        data[0][n] = tmp_data

    true_points2 = data_trans.analysis_data(true_line2)
    points = get_velocity(true_points2)
    true_num = random.choice(range(20))
    for point in points:
        data[1][true_num][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100,
                                                                                   point['v']]

    tmp = list(range(30))
    tmp.remove(x * 10 + y)
    rand_classes = np.random.choice(tmp, size=(19,))
    z_2_fs = list(range(20))
    z_2_fs.remove(true_num)
    for i in range(19):
        rand_class = rand_classes[i]
        x_2_f = int(rand_class / 10)
        y_2_f = rand_class % 10
        false_line = all_lines[x_2_f - 1][y_2_f - 1][random.randint(0, 19)]
        false_points = data_trans.analysis_data(false_line)
        false_points = get_velocity(false_points)
        for point in false_points:
            data[1][z_2_fs[i]][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100,
                                                                                        point['v']]


create_mul2()
