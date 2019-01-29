import time

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import data_trans

data = data_trans.analysis_data('_ey_gd_2g_3u_lf_m4_n2_ta_nz_ng_me_4x_32_2c_gw_fw_f4_gh_h3_2u_4g_lx_nh_tl_ue_u3_uh_uf_3f_3b_2t_2m_2n_2y_3h_4c_lb_mf_nw_ul_xh_yxbaebbfbblbbcbal_zy_zg_yn_yb_x4_xf_xc_xh_xa_aa_cy_dw_en_f3_gg_he_2a_2x_3n_44_lg_md_na_nx_tt_u4bbhbcfbdbbdzbexbfnbglbhgb3cbmhbxh')
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
