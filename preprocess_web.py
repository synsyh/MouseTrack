import numpy as np
import math
import data_trans


def get_velocity(ps):
    for i in range(len(ps) - 2):
        ps[i + 1]['v'] = math.sqrt((ps[i + 2]['x'] - ps[i]['x']) ** 2 + (ps[i + 2]['y'] - ps[i]['y']) ** 2) / (
                ps[i + 2]['time'] - ps[i]['time'])
    ps[0]['v'] = 0
    ps[-1]['v'] = ps[-2]['v']
    return ps


if __name__ == '__main__':
    points_data = np.zeros((300, 420, 530, 3))
    with open('./data/sun2', 'r') as f:
        for i, line in enumerate(f.readlines()):
            points = data_trans.analysis_data(line)
            points = sorted(points, key=lambda x: x['time'])
            points = get_velocity(points)
            for point in points:
                points_data[i][point['x']][point['y']] = [1, point['time'], point['v']]
    np.save('./data/data_web_sun', points_data)
