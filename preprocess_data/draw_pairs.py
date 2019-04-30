import os
import json
from utils import data_trans
import matplotlib.pyplot as plt

with open('error_drawers.json') as f:
    data = f.read()
drawers = json.loads(data)
char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# d = {}
# for c in char_list:
#     d[c] = []
# for path in paths:
#     c = path['char']
#     d[c].append(path['path'])
#
# rp = '../img_a/'
# for _, char_paths in d.items():
#     if _ == 'a':
#         rp = '../img_b/'
#     plt.figure(figsize=(24, 8))
#     for i, char_path in enumerate(char_paths):
#         plt.subplot(130 + i + 1)
#         ps = data_trans.analysis_data(char_path)
#         x = [ps[i]['x'] for i in range(len(ps))]
#         y = [-ps[i]['y'] for i in range(len(ps))]
#         plt.plot(x, y)
#     plt.savefig(rp + _ + '.jpg')
#     plt.close()

for id, drawer in drawers.items():
    rp = ''
    for char in char_list:
        if char == 'a':
            rp = '_'
        paths = drawer[char]
        plt.figure(figsize=(24, 8))
        for i, path in enumerate(paths):
            plt.subplot(130 + i + 1)
            ps = data_trans.analysis_data(path)
            x = [ps[i]['x'] for i in range(len(ps))]
            y = [-ps[i]['y'] for i in range(len(ps))]
            plt.plot(x, y)
        img_dir_path = 'img/' + id + '/'
        isExists = os.path.exists(img_dir_path)
        if isExists:
            plt.savefig('img/' + id + '/' + char + rp + '.jpg')
        else:
            os.makedirs(img_dir_path)
            plt.savefig('img/' + id + '/' + char + rp + '.jpg')
        plt.close()
