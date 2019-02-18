import numpy as np

import keras

import data_trans
from siamese_preprocess import get_velocity


def get_inputs():
    x_ratio = 0.27367970921530893
    y_ratio = 0.2158152082279548
    first_line = '_f2_gc_gt_3g_3x_43_4z_l2_lu_lz_lz_ly_l3_4w_4b_3e_2f_he_gc_fb_dh_ct_ch_cn_d2_ee_f3_gx_2g_3t_4z_ma_mu_ng_nn_nz_4b_3g_2z_2g_2g_22_2u_3e_3w_lb_lw_mm_n2_tg_uf_we_xa_xu_yh_yx_z3_zn_zu_zw_zw_zw_zw_zn_zm_zl_zl_z4_z3_z3_z3_z3_aa_bu_c4_g3_gm_h2_2e_3b_3x_ll_m2_ne_tb_ty_uu_wm_x2_yf_zc_zybbmbc2bdfbglbh2b2fb3cb3yb4ublmbm2bnfbtcbtybuubx2'
    line_list = ['_f2_f4_fw_gc_g4_gy_h3_2a_2n_32_4a_4m_le_lx_mh_mt_mx_mx_mt_mf_lm_4y_4c_3e_2f_hf_gd_ff_e2_dy_dm_e2_f4_gz_2n_4a_lh_mn_nw_tm_ud_u3_lc_4x_4g_3z_3l_3e_2y_2t_24_22_22_22_2t_3e_3u_44_lh_mh_n4_tn_uu_wn_x2_ya_y4_yy_zg_z4_zm_zn_zt_zt_zm_zl_z4_z4_z4_z4_z4_zl_zl_zn_aa_bf_cy_dw_em_f3_gf_hc_hz_2u_3t_43_lf_mc_mz_nu_tl_u2_wf_xb_xy_yw_zmba3bbgbccbczbdwbenbf3bggb3mb42blfbmbbmybnubtlbu2bwfbxcbxz',
                 '_ft_fu_fw_gd_g4_gx_he_hm_2b_2m_3d_3u_44_lc_lu_mf_mt_na_ne_nh_nh_nf_mx_m2_ly_lf_44_3n_2m_hu_gw_fx_fa_eh_dy_dm_ed_ey_fw_hb_2h_3n_4x_mb_mz_nw_tf_tl_ln_lg_lb_44_4a_3l_3c_2t_22_2d_2a_hx_hw_hw_hz_2g_2z_3n_44_lt_mw_nz_ua_uz_wt_xh_xy_yg_yn_yx_zb_ze_zg_z2_z4_z4_z4_z4_z4_z3_z2_z2_z2_z2_zh_zg_zg_zg_aa_cb_cy_em_f2_gf_hc_hy_2u_3m_42_lf_mc_my_nu_tm_u2_wf_xc_xy_yu_zmba2bbfbccbcybdubembf2bgfbhcbhyb2ub3mb42blfbu2bwfbxcbxybyubzmca2cbfcccccycducem',
                 '_2b_3g_4m_lx_mu_nd_ne_mz_lz_4h_24_gt_fe_eg_dx_dn_fc_hd_3f_lc_m3_nt_tu_ul_4d_4n_ld_ly_mw_nl_th_ue_wb_xa_ya_zbbabbatbbcbbgbbebaxbamba3bagbab_zw_zn_aa_ax_bu_c3_df_ea_ew_fm_g3_hg_2d_3f_3u_4m_lm_mg_tw_un_w4_xg_yd_za_zwban',
                 '_2f_2t_3h_4g_lh_mf_mu_ly_4h_2t_ha_fy_fd_ew_gd_2b_3z_ln_my_td_4g_4l_4m_la_ln_mh_mz_ub_w4_xl_yl_zd_zm_zx_zy_zl_zg_zg_zg_zg_aa_b2_cf_db_dy_eu_h2_2b_2y_3w_4m_l3_mf_nc_ul_w3_xh_yc_yy_zu',
                 '_t3_tc_nt_ng_mw_md_l2_4m_4a_3t_3m_3m_3m_3n_3t_3t_3m_3d_2m_hm_hh_he_hc_hc_he_hu_2u_3x_lc_mm_t3_we_xm_yz_zxba4bbabbe_aa_a4_bf_cc_cz_dw_em_f3_gg_hc_hz_2w_3n_43_lg_mc_mz_nw_tm']
    data = [np.zeros((len(line_list), 128, 128, 3)) for i in range(2)]
    first_points = data_trans.analysis_data(first_line)
    first_points = get_velocity(first_points)
    for i in range(len(line_list)):
        for point in first_points:
            data[0][i][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]

    for i, line in enumerate(line_list):
        points = data_trans.analysis_data(line)
        points = get_velocity(points)
        for point in points:
            data[1][i][int(point['x'] * x_ratio)][int(point['y'] * y_ratio)] = [1, point['time'] / 100, point['v']]
    return data

model = keras.models.load_model('weights2')
inputs = get_inputs()
probs = model.predict(inputs)
print(probs)
