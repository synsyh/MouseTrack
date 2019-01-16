import copy
import math

with open('./data/MouseTrack_S.txt') as f:
    with open('./data/clean_data.txt', 'w') as w:
        for line in f.readlines():
            line = line[2:-3]
            tmp = line.split('], [')
            points = [n.split(',')[:-1] for n in tmp]
            time = [n.split(',')[-1:] for n in tmp]
            start_time = copy.copy(time[1][0])
            for t in time[1:]:
                t[0] = float(t[0]) - float(start_time)
            points = points[1:]
            time = time[1:]
            v = []
            v.append(0.0)
            w.write('(' + str(int(points[0][0])) + ',' + str(int(points[0][1])) + ')' + ',' + str(v[0]) + ',' + str(
                time[0][0]) + '\n')
            for i, point in enumerate(points[:-2]):
                dis = math.sqrt((float(points[i + 2][0]) - float(point[0])) ** 2 + (
                        float(points[i + 2][1]) - float(point[1])) ** 2)
                v.append(dis / (time[i + 2][0] - time[i][0]))
                w.write('(' + str(int(point[0])) + ',' + str(int(point[1])) + ')' + ',' + str(v[-1]) + ',' + str(
                    time[i + 1][0]) + '\n')
            w.write('(' + str(int(points[-1][0])) + ',' + str(int(points[-1][1])) + ')' + ',' + str(v[-1]) + ',' + str(
                time[-1][0]) + '\n')
            w.write('*****\n')
