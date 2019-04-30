# 实时再绘制轨迹
from utils import data_trans
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
    raw_data = 'bbmbbnbbxbcbbcebc2bcmbcubczbddbdhbdlbdubdybecbegbe3benbexbfbbfebf2bfmbfwbfzbgdbg2bgnbgybhebh3bhtb2ab2fb23b2mb2xb3cb3gb33b3tb3xb4bb4fb42b4lb4lb4lb4lb4nb4ybldbl3blmblmblmblmblmbl3bldb4xb4mb4hb4bb3wb3lb3fb2zb2tb22b2dbhzbhnbhhbhbbgwbg4bgebfzbfubflbfgbfabetbe3bedbanbazbbcbbgbb4bbtbbxbcbbcfbc3bcnbcwbdabdebd2bdlbdubdzbecbegbe4betbexbfbbffbf3bflbflbflbflbflbflbflbflbfhbfdbfcbezbewbembe2beebeabdwbdnbd2bdcbcxbcmbchbcgbcgbcfbccbbwbb4bbfbazbaubatbatbatbatbatbatbatbatbatbatbawbbbbbdbbdbbdbbdbbdbbdbbdbbdbb2bblbbnbbnbbnbbnbbn_aa_ew_gx_2z_lb_nd_ul_x4_z3bbybdzbgcb2db4gbmlbt3bwtbyncbaccxcfbchbc3hclfcnlcu3cyddbedefdhdd4hdnddwedzeebfed2egde2weleenaeu2exlezlfbufdwfg3f3mfmlfu4fxzgalgdwggtg2wgmdgubgybhblhd3hg2h3whmnhwahyx2bt2eu22f24z2tc2xg3aa3cn3fu33a3mn3un3ym4bx4ez4h243h4mn4ut4ytlbtlfa   '
    points = data_trans.analysis_data(raw_data)
    points = data_trans.scale(points)
    draw(points)
