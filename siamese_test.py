import numpy as np

import keras

import data_trans
from siamese_preprocess import get_velocity


def get_inputs():
    x_ratio = 0.27367970921530893
    y_ratio = 0.2158152082279548
    data = [np.zeros((2, 128, 128, 3)) for i in range(2)]
    true_line = '_n3_my_mb_4m_3a_hm_gu_ge_ga_ga_gf_hd_22_4e_lu_mt_ng_nm_nn_ne_ma_4n_3b_hy_gu_3f_3d_3h_4e_le_me_my_n3_ny_th_tw_uh_wa_ww_x3_xy_yf_y4_yu_zf_zybalbbebbmbbw_aa_ce_df_eh_em_f2_ge_hb_hx_2t_3l_4h_le_mb_my_nt_tl_uh_we_xa_xx_yt_z4bahbbe _ng_mu_mc_4z_3f_hu_gu_gb_fu_ft_ga_hf_3c_4u_lz_nc_nx_tg_t2_td_na_lh_4b_2n_3d_3c_3g_3y_la_mc_mz_nl_ta_th_tx_u3_we_ww_xh_ya_ym_zc_zmbahbbdbbubbybby_aa_b4_ch_dd_ea_ey_ft_gl_hh_2g_3b_3y_4u_ll_mh_nd_ta_tx_ut_wl_xh_ye_zb_zy'
    true_points1 = data_trans.analysis_data(true_line.split(' ')[0])
    true_points2 = data_trans.analysis_data(true_line.split(' ')[1])
    true_points1 = get_velocity(true_points1)
    true_points2 = get_velocity(true_points2)
    for point in true_points1:
        data[0][0][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    for point in true_points2:
        data[1][0][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]

    false_line = '_n3_my_mb_4m_3a_hm_gu_ge_ga_ga_gf_hd_22_4e_lu_mt_ng_nm_nn_ne_ma_4n_3b_hy_gu_3f_3d_3h_4e_le_me_my_n3_ny_th_tw_uh_wa_ww_x3_xy_yf_y4_yu_zf_zybalbbebbmbbw_aa_ce_df_eh_em_f2_ge_hb_hx_2t_3l_4h_le_mb_my_nt_tl_uh_we_xa_xx_yt_z4bahbbe _fz_fy_ge_hb_2a_3a_3n_4t_l4_lx_lz_ly_ll_4t_3m_2m_ht_ha_gf_gd_g4_hd_2h_3f_4t_lt_mx_td_ud_me_lx_4y_3w_3e_3d_3g_3x_44_l2_me_nb_tm_um_wy_yb_zebafbaybbebbgbbdba3bab_zb_ye_x3_wx_wb_aa_cn_dm_e2_ff_gb_gy_hu_2m_33_4f_lc_ma_mw_nn_t3_uf_wd_xa_yn_zlbahbbebccbczbdxbe4bf3bhe'
    false_points1 = data_trans.analysis_data(false_line.split(' ')[0])
    false_points2 = data_trans.analysis_data(false_line.split(' ')[1])
    false_points1 = get_velocity(false_points1)
    false_points2 = get_velocity(false_points2)
    for point in false_points1:
        data[0][1][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    for point in false_points2:
        data[1][1][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    return data


model = keras.models.load_model('weights1')
inputs = get_inputs()
probs = model.predict(inputs)
print()
