# 检查数据的最大值最小值
import pandas as pd
import data_trans


def get_size(file_path):
    x_min = 1000
    x_max = 0
    y_min = 1000
    y_max = 0
    with open(file_path, 'r') as f:
        for i, line in enumerate(f.readlines()):
            ps = data_trans.analysis_data(line)
            dt = pd.DataFrame(ps)
            x_min = min(x_min, dt['x'].min())
            x_max = max(x_max, dt['x'].max())
            y_min = min(y_min, dt['y'].min())
            y_max = max(y_max, dt['y'].max())
    return x_min, y_min, x_max*1.1+20, y_max*1.1+20


def get_scale_ratio(file_paths, width=128, height=128):
    if type(file_paths).__name__ == 'list':
        x_max = 0
        y_max = 0
        for file_path in file_paths:
            _, _, x_max_tmp, y_max_tmp = get_size(file_path)
            x_max = max(x_max, x_max_tmp)
            y_max = max(y_max, y_max_tmp)
        width_ratio = width / x_max
        height_ratio = height / y_max
    else:
        _, _, x_max, y_max = get_size(file_paths)
        width_ratio = width / x_max
        height_ratio = height / y_max
    print(x_max, y_max)
    return width_ratio, height_ratio


if __name__ == '__main__':
    w, h = get_scale_ratio(['./data/sun2', './data/yuan2', './data/yu2'])
    print(w, h)
