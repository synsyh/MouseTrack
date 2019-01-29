# 实时再绘制轨迹
import data_trans
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def draw(raw_data):
    if type(raw_data).__name__ == 'str':
        data = data_trans.analysis_data(raw_data)
    else:
        data = raw_data
    xs = [data[0]['x']]
    ys = [-data[0]['y']]
    for i in range(len(data) - 1):
        dis_x = data[i + 1]['x'] - data[i]['x']
        dis_y = data[i + 1]['y'] - data[i]['y']
        n = (data[i + 1]['time'] - data[i]['time']) / 10
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
    for i in range(int(data[-1]['time'] / 10) + 1):
        plt.clf()
        plt.plot(max_x, max_y)
        plt.plot(min_x, min_y)
        plt.plot(xs[:i], ys[:i])
        plt.pause(0.001)
        plt.ioff()
    plt.clf()
    plt.plot(xs, ys)
    plt.show()


if __name__ == '__main__':
    draw(
        '_fm_fz_g3_gx_hg_ht_2b_23_2w_3d_33_3w_4c_42_4u_la_ld_ld_la_4t_4g_3w_3e_2n_2b_hl_ha_gm_gg_gb_ga_gc_gg_gl_gz_h4_2e_2y_3n_42_lc_lt_md_m2_mu_3n_3d_2m_2f_2a_hx_hw_hw_hx_2a_2d_22_2t_3d_3u_44_lg_md_nb_tb_uc_wb_xa_xw_y3_yy_ze_zf_zd_yw_yl_ye_xw_x4_xd_wx_wt_wn_wu_wy_xc_xf_x2_xl_xu_aa_cl_dl_e4_fe_ga_gx_ht_24_33_4e_ln_md_mx_ny_tu_ul_wc_ww_xm_y4_zhbafbazbbxbctbdlbegbfbbgwbhmb2lb3fb4bb4zbltbmlbn2btebucbwabwtbxnbyxcah')
