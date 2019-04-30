# 制作假数据
import math
import random

import pandas as pd

from utils import data_trans
from utils import draw_time


def point_rotate(angle, x, y, point_x, point_y):
    """
    点绕点旋转
    :param angle:角度
    :param x:输入的点
    :param y:
    :param point_x:绕旋转的点
    :param point_y:
    :return:
    """
    rotate_x = (x - point_x) * math.cos(angle) + (y - point_y) * math.sin(angle) + point_x
    rotate_y = (y - point_y) * math.cos(angle) - (x - point_x) * math.sin(angle) + point_y
    return rotate_x, rotate_y


def create_fake(ps):
    x_min = 1000
    x_max = 0
    y_min = 1000
    y_max = 0
    bias_ratio = random.randint(-10, 10)
    rotate_ratio = math.radians(random.randint(-30, 30))
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
        x = (x - x_mid) * math.cos(rotate_ratio) + (y - y_mid) * math.sin(rotate_ratio) + x_mid
        y = (y - y_mid) * math.cos(rotate_ratio) - (x - x_mid) * math.sin(rotate_ratio) + y_mid
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
    # with open('./data/track1000', 'r') as f:
    #     with open('./data/fake_track_s', 'w') as w:
    #         for i, line in enumerate(f.readlines()):
    #             points = data_trans.analysis_data(line)
    #             for j in range(10):
    #                 points = create_fake(points)
    #                 points = sorted(points, key=lambda x: x['time'])
    #                 points = get_velocity(points)
    #                 w.write()
    # test one data
    raw_data = '_2x_23_2h_2w_3f_3z_4w_lu_nd_tb_tl_tu_ty_tx_t4_nz_na_me_ll_44_33_2f_hw_hh_he_2h_32_4u_lu_mw_n4_nw_td_w2_u3_td_mz_ma_ld_4l_3z_3z_4b_4g_4t_ld_mb_nd_ty_wf_xn_yx_zxbaxbbnbc3bcwbdabcfbbtbbgbazbanba2bafbad_aa_dh_ef_fa_fy_gu_hm_22_3f_4c_4z_lw_mt_n4_th_ud_uz_ww_xt_yl_zhbadbbbbbxbcubgbbgybhxb2lb34b4fbldbmy'
    points = data_trans.analysis_data(raw_data)
    points = create_fake(points)
    draw_time.draw(points)
