import numpy as np

import keras

import data_trans
from siamese_preprocess import get_velocity


def get_inputs():
    x_ratio = 0.27367970921530893
    y_ratio = 0.2158152082279548
    data = [np.zeros((2, 128, 128, 3)) for i in range(2)]
    true_line1 = '_et_fe_ha_2f_3l_4x_lw_m4_mz_nc_nc_mu_mf_l3_42_3e_2c_hg_gm_gc_fu_fl_f3_gb_he_2w_43_md_nn_tu_uu_w4_wy_44_3z_3d_2w_2m_2l_2l_2t_3c_3m_4g_lf_mf_ng_tt_wb_xg_yh_zhbaaba4baxbbdbbcbanbaa_zg_yl_xz_x3_xb_ww_wt_aa_ax_cm_d2_ee_fb_fy_gu_hm_22_3f_4c_4y_lu_mm_n2_tf_ux_uz_wt_xl_yhbabbaybbubclbd2befbfcbfybgubhmb22'
    true_line2 = '_fe_ga_hb_2h_3u_4z_lx_m3_mx_mz_mx_me_lh_4d_2x_hl_gh_f4_ez_en_em_fx_hc_2u_42_mc_nx_u3_wn_xm_ye_y4_32_3e_3e_3e_3e_3e_3h_3n_4d_4w_lu_my_tb_u2_wm_xx_yz_zwba3baxbbcbbbbanbae_zt_zd_y4_xy_x4_xe_xc_xc_aa_bl_ch_dd_ea_ex_ft_g4_hh_2e_3a_3x_4t_l4_m2_ne_tb_tx_ut_wl_xh_zb_zybatbblbc2bdebebbeybfubglbh2'
    true_points1 = data_trans.analysis_data(true_line1)
    true_points2 = data_trans.analysis_data(true_line2)
    true_points1 = get_velocity(true_points1)
    true_points2 = get_velocity(true_points2)
    for point in true_points1:
        data[0][0][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    for point in true_points2:
        data[1][0][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]

    false_line1 = '_d2_dm_dy_el_fn_hb_2m_3t_44_lc_ll_lw_lx_lx_lt_l2_lc_4u_4e_3t_2y_2f_h4_gz_g2_fx_f4_fd_ew_fh_gb_gw_hl_2h_3f_4h_l2_m4_nn_tm_uf_uw_wc_wh_nu_mu_mc_lg_4c_2y_hy_hh_he_he_h2_hy_2t_34_42_lg_mc_mz_ny_tn_ul_wd_wt_xd_xl_xz_yf_y4_yu_yn_ym_yl_yl_yl_yl_yl_yl_yl_yl_y4_yh_yg_ye_yd_aa_bd_bg_cd_da_dw_em_f3_gf_hc_hz_2w_3m_43_lg_mc_mz_nw_tn_u4_wg_xd_ya_yx_znba4bbgbcdbdwb2xb3nb44blhbmdbnabnxbtnbu4bwhbxdbyabyxbznca4'
    false_line2 = '_dh_dd_de_dw_fc_gl_2a_3d_4g_lf_me_mz_n4_nu_nw_nw_nm_ne_mt_mb_ld_4e_3b_hz_gy_ga_fh_ew_e3_ee_ew_fm_gt_hy_3d_42_l4_mf_mx_n3_ny_tf_tm_td_nl_nc_mf_4y_3m_24_hy_h4_h2_h2_hu_2f_2x_34_4h_ld_ly_mn_nh_te_ub_uy_wt_xh_xz_yg_yl_yu_yy_yy_yy_yy_yz_za_zc_ze_zg_zh_zh_zh_zh_zh_aa_be_ca_cx_du_el_fh_ge_ha_hx_2n_34_4h_le_ma_mx_nt_t4_uh_wd_xa_xx_yt_z4bahbbdbcabcxbdtbelb34b4hbldbmabmybnnbt4buhbwdbxabxxbytca3'
    false_points1 = data_trans.analysis_data(false_line1)
    false_points2 = data_trans.analysis_data(false_line2)
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
print(probs)
