import time

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import data_trans

data = data_trans.analysis_data('_eb_e2_ey_ft_hd_2w_4l_mc_ne_ta_te_ny_mw_lf_3l_2b_hf_hb_hh_3a_le_nh_u4_xa_ya_y3_3e_2y_2l_2d_hl_hh_hh_hx_2n_3w_l4_nw_wd_y4baubcmbdmbebbedbd2bcdbaw_zn_yx_y2_yf_aa_a4_am_at_b4_ch_de_ed_ey_fu_gl_h2_2e_3b_3y_4t_ln_mh_ng_tb_tx_ut_wm_x2_ye_zd')
xs = [data[0]['x']]
ys = [-data[0]['y']]
for i in range(len(data) - 1):
    dis_x = data[i + 1]['x'] - data[i]['x']
    dis_y = data[i + 1]['y'] - data[i]['y']
    n = (data[i + 1]['time'] - data[i]['time'])/10
    step_x = dis_x / n
    step_y = dis_y / n
    tmp_x = data[i]['x']
    tmp_y = data[i]['y']
    for j in range(int(n)):
        tmp_x += step_x
        tmp_y += step_y
        xs.append(tmp_x)
        ys.append(-tmp_y)
xs.append(data[-1]['x'])
ys.append(-data[-1]['y'])
max_x = max(xs)
min_x = min(xs)
max_y = max(ys)
min_y = min(ys)
plt.ion()
for i in range(int(data[-1]['time']/10) + 1):
    plt.clf()
    plt.plot(max_x, max_y)
    plt.plot(min_x, min_y)
    plt.plot(xs[:i], ys[:i])
    plt.pause(0.001)
    plt.ioff()
plt.clf()
plt.plot(xs, ys)
plt.show()
