import numpy as np
import math


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
    x = np.array(x)
    y = np.array(y)
    rotate_x = (x - point_x) * math.cos(angle) + (y - point_y) * math.sin(angle) + point_x
    rotate_y = (y - point_y) * math.cos(angle) - (x - point_x) * math.sin(angle) + point_y
    return rotate_x, rotate_y


print(point_rotate(45, 0, 2, 0, 0))
