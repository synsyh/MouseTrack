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
        '_2x_23_2h_2w_3f_3z_4w_lu_nd_tb_tl_tu_ty_tx_t4_nz_na_me_ll_44_33_2f_hw_hh_he_2h_32_4u_lu_mw_n4_nw_td_w2_u3_td_mz_ma_ld_4l_3z_3z_4b_4g_4t_ld_mb_nd_ty_wf_xn_yx_zxbaxbbnbc3bcwbdabcfbbtbbgbazbanba2bafbad_aa_dh_ef_fa_fy_gu_hm_22_3f_4c_4z_lw_mt_n4_th_ud_uz_ww_xt_yl_zhbadbbbbbxbcubgbbgybhxb2lb34b4fbldbmy')
