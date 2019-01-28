import pandas as pd
import data_trans

data = {}
x_min = 1000
x_max = 0
y_min = 1000
y_max = 0
with open('./data/yuan2', 'r') as f:
    for i, line in enumerate(f.readlines()):
        ps = data_trans.analysis_data(line)
        ps = sorted(ps, key=lambda x: x['time'])
        dt = pd.DataFrame(ps)
        data[i] = dt
        x_min = min(x_min, dt['x'].min())
        x_max = max(x_max, dt['x'].max())
        y_min = min(y_min, dt['y'].min())
        y_max = max(y_max, dt['y'].max())
print(x_min, y_min)
print(x_max, y_max)
print()
