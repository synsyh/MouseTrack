# 解密数据
import math
import numpy as np


Sample = "abcdefgh234lmntuwxyz"
file_path = './data/track1000'


def get_velocity(ps):
    """
    得到points的速度
    :param ps:
    :return: 加了速度的points list
    """
    for i in range(len(ps) - 2):
        try:
            v = math.sqrt((ps[i + 2]['x'] - ps[i]['x']) ** 2 + (ps[i + 2]['y'] - ps[i]['y']) ** 2) / (
                    ps[i + 2]['time'] - ps[i]['time'])
        except Exception as e:
            print(e)
            v = 0
        ps[i + 1]['v'] = v
    ps[0]['v'] = 0
    ps[-1]['v'] = ps[-2]['v']
    return ps


def trans_from_data(code):
    scale = len(Sample)
    length = int(len(code))
    result = 0
    for i in range(int(length / 3)):
        if i == 0 and code[i] == '_':
            result = Sample.index(code[i + 1]) * \
                     scale + Sample.index(code[i + 2])
        else:
            result = Sample.index(code[i]) * scale * scale + Sample.index(
                code[i + 1]) * scale + Sample.index(code[i + 2])
    return result


def analysis_data(code):
    """
    轨迹转化
    :param code: 轨迹字符串
    :return: 点的字典，包括x, y, time
    """
    length = int(len(code) / 9)
    points = []
    for i in range(length):
        ix = i * 3
        iy = i * 3 + length * 3
        it = i * 3 + 2 * length * 3
        x = code[ix:ix + 3]
        y = code[iy:iy + 3]
        t = code[it:it + 3]

        points.append({'x': int(trans_from_data(x)), 'y': int(trans_from_data(y)), 'time': int(trans_from_data(t))})

    return points


def scale(points, if_zero=False):
    """
    将所有的点归一化为边界120
    :param points: 点
    :param if_zero:
    :return: 归一化后的点list
    """
    boundary = 120
    y_min = min(points, key=lambda x: x['y'])['y']
    y_max = max(points, key=lambda x: x['y'])['y']
    x_min = min(points, key=lambda x: x['x'])['x']
    x_max = max(points, key=lambda x: x['x'])['x']
    if x_max - x_min > y_max - y_min:
        dis = x_max - x_min
    else:
        dis = y_max - y_min
    scale_ratio = boundary / dis
    new_points = []
    if if_zero:
        for point in points:
            new_points.append({'x': int((point['x'] - points[0]['x']) * scale_ratio),
                               'y': int((point['y'] - points[0]['y']) * scale_ratio),
                               'time': point['time']})
    else:
        for point in points:
            new_points.append(
                {'x': int((point['x'] - x_min) * scale_ratio), 'y': int((point['y'] - y_min) * scale_ratio),
                 'time': point['time']})
    return new_points


def trans2matrix(points):
    data = np.zeros((128, 128, 3))
    for point in points:
        data[int(point['x'])][int(point['y'])] = [1, point['time'] / 100,
                                                  point['v']]
    return data


if __name__ == '__main__':
    ps = get_velocity(analysis_data(
        'cczccnccgcbzcblcaycamcabbzubzhbzabytby2bycbxxbxlbxgbxbbwwbwtbwnbwnbwubwzbxebx4bxwbygbyubzdbz2bzmbzwbzzcaeca3ca3camcamcancaucawcaycbacbccbfcb2cb3_za_yw_yw_yu_yu_ym_yl_yg_ye_yb_xy_xu_xn_x4_x3_xh_xd_xa_wn_w2_wd_uu_u3_ud_ty_tu_tt_tt_tu_ub_uf_u3_ut_wa_wg_wt_xd_xn_xz_ye_ym_yx_zc_z2_zxbadba3bat_aa_fw_hw_3z_ln_td_ua_x4_zdbawbc4bedbfwb3dbm4bxlcclc2hc4xcmlcteczedfbdhldmlduxdzeeclehle4yemleteeuyexlezefaxfclfeeffyfhlf4yfmlftefuyfzfgaxgeehbm'))
    print()
