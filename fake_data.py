import numpy as np
import pandas as pd
import math
import data_trans
import random


def get_velocity(ps):
    for i in range(len(ps) - 2):
        ps[i + 1]['v'] = math.sqrt((ps[i + 2]['x'] - ps[i]['x']) ** 2 + (ps[i + 2]['y'] - ps[i]['y']) ** 2) / (
                ps[i + 2]['time'] - ps[i]['time'])
    ps[0]['v'] = 0
    ps[-1]['v'] = ps[-2]['v']
    return ps


def create_fake(ps):
    x_min = 1000
    x_max = 0
    y_min = 1000
    y_max = 0
    bias_ratio = random.randint(-10, 10)
    rotate_ratio = random.randint(-10, 10)
    resize_ratio = random.randint(-10, 10)
    dt = pd.DataFrame(ps)
    x_min = min(x_min, dt['x'].min())
    x_max = max(x_max, dt['x'].max())
    y_min = min(y_min, dt['y'].min())
    y_max = max(y_max, dt['y'].max())
    x_mid = (x_min + x_max) / 2
    y_mid = (y_min + y_max) / 2
    for p in ps:
        x = p['x']
        y = p['y']
        # rotate
        # x = (x - x_mid) * math.cos(math.radians(rotate_ratio)) - (y - y_mid) * math.sin(math.radians(rotate_ratio)) + x
        # y = (x - x_mid) * math.sin(math.radians(rotate_ratio)) + (y - y_mid) * math.cos(math.radians(rotate_ratio)) + y
        # resize
        x += (x - x_mid) * resize_ratio / 100
        y += (y - y_mid) * resize_ratio / 100
        # bias
        x += bias_ratio
        y += bias_ratio
        p['x'] = int(x)
        p['y'] = int(y)
    return ps


if __name__ == '__main__':
    with open('./data/track1000', 'r') as f:
        with open('./data/fake_track_s', 'w') as w:
            for i, line in enumerate(f.readlines()):
                points = data_trans.analysis_data(line)
                for j in range(10):
                    points = create_fake(points)
                    points = sorted(points, key=lambda x: x['time'])
                    points = get_velocity(points)
                    w.write()
