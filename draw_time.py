import time

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import data_trans

data = data_trans.analysis_data('_uc_tm_nz_nc_ly_4m_32_22_hl_gz_gw_gy_h3_2g_32_43_lt_mt_nm_tg_tn_tn_t3_nn_ml_lc_33_hu_gd_fc_e2_ec_3l_3d_2z_2w_2u_2u_2w_3h_4c_lb_md_nh_tl_um_wl_xh_yf_zbbaabbabbxbcubdnbeubfubg4bgybhabgzbglbfxbex_aa_bc_bz_cx_du_em_f2_gd_hb_hx_2t_34_4f_lc_lz_mu_nm_t3_ug_wc_wz_xw_ym_z3bafbbcbbzbcubdmbe3bffbgc')
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
