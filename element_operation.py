# 泡泡界面中单个元素的一些操作

import ball_def as BALL
import random


def get_neib(one_line_chess, r, c):
    '''
    获得r行c列元素的邻居集合
    :param one_line_chess:
    :param r: 直接以array形式计算，第一行r=0
    :param c: 列数
    :return: 以[[],[]...]形式返回[r,c]的周边邻居
    '''
    d = BALL.BALLS_PER_ROW
    rows = int(len(one_line_chess) / d)
    neib = []

    neib.append([r, c - 1])
    neib.append([r, c + 1])  # 左右
    neib.append([r - 1, c])  # 偶数行右上，奇数行左上
    neib.append([r + 1, c])  # 偶数行右下，奇数行左下
    if r % 2 == 0:
        neib.append([r - 1, c - 1])  # 上面左下
        neib.append([r + 1, c - 1])  # 下面左上
    else:
        neib.append([r - 1, c + 1])  # 上面右上
        neib.append([r + 1, c + 1])  # 下面右下

    valid_neib = []
    for i in range(len(neib)):
        rr, cc = neib[i][0], neib[i][1]
        # 超出行数边界
        if rr < 0 or rr >= rows:
            continue

        # 超出列数边界
        right_end = d if rr % 2 == 0 else d - 1
        if cc < 0 or cc >= right_end:
            continue

        valid_neib.append(neib[i])

    return valid_neib


def get_empty_pos(one_line_chess, r, c):
    '''
    返回[r, c]点上周边可填泡泡的邻居坐标集
    :param one_line_chess:
    :param r: 直接以array形式计算，第一行r=0
    :param c: 列数
    :return: 以[[],[]...]形式返回[r,c]周边邻居中可填的点位
    '''
    neib = get_neib(one_line_chess, r, c)

    valid_neib = []
    for i in range(len(neib)):
        rr, cc = neib[i][0], neib[i][1]
        # 非彩色泡泡
        if one_line_chess[rr * BALL.BALLS_PER_ROW + cc] != BALL.ELEMENT_INIT:
            continue

        valid_neib.append(neib[i])

    return valid_neib


def get_color_neibs(one_line_chess, r, c):
    '''
    得到邻居中是彩色泡泡的集合
    :param one_line_chess:
    :param r: 直接以array形式计算，第一行r=0
    :param c: 列数
    :return: 以[[],[]...]形式返回[r,c]的周边非空的邻居集合
    '''
    neib = get_neib(one_line_chess, r, c)

    valid_neib = []
    for i in range(len(neib)):
        rr, cc = neib[i][0], neib[i][1]
        # 非彩色泡泡
        if one_line_chess[rr*BALL.BALLS_PER_ROW+cc] <= 0:
            continue

        valid_neib.append(neib[i])

    return valid_neib


# 在邻居中随机选择下一个未填色的位置
def random_next_empty_neib(one_line_chess, r, c):
    options = get_empty_pos(one_line_chess, r, c)

    # 随机选择一个邻居
    if len(options)>0:
        newpos = options[random.randint(0, len(options)-1)]
        return True, newpos[0], newpos[1]
    # 已无有效的空元素
    else:
        return False, 0, 0