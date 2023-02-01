# 将整个泡泡游戏界面看成是一个n行11列的棋盘.该文件是对整个棋盘的一些操作

import ball_def as BALL
import element_operation as eo
import random
import util


def mirrorX(array_chess):
    '''
    水平方向的镜像.以第6列为轴，将左半边的镜像到右半边
    :param array_chess: 代表泡泡游戏界面的二维矩阵
    :return:
    '''
    rows, cols = len(array_chess), BALL.BALLS_PER_ROW
    for r in range(rows):
        line = array_chess[r]
        reverse_line = line[::-1]
        if r % 2 == 0:
            line[6:BALL.BALLS_PER_ROW] = reverse_line[6:BALL.BALLS_PER_ROW]
        else:
            line[5:BALL.BALLS_PER_ROW-1] = reverse_line[6:BALL.BALLS_PER_ROW]
        array_chess[r] = line

    return array_chess


#
def remove_single_ball(oneline_chess):
    '''
    将游戏中可能存在的单个泡泡的颜色改为和周边颜色最多的一致
    :param oneline_chess: 以一行表示的泡泡布局
    :return: 去除了单个泡泡的谜面
    '''
    d = BALL.BALLS_PER_ROW
    rows = int(len(oneline_chess) / d)

    for i in range(len(oneline_chess)):
        cur_clr = oneline_chess[i]
        if cur_clr <= 0:
            continue

        rr, cc = int(i / BALL.BALLS_PER_ROW), int(i % BALL.BALLS_PER_ROW)
        neib = eo.get_color_neibs(oneline_chess, rr, cc)
        if len(neib) == 0:
            continue

        neib_clrs = []
        for j in range(len(neib)):
            row, col = neib[j][0], neib[j][1]
            neib_clrs.append(oneline_chess[row*BALL.BALLS_PER_ROW+col])

        # 如果是单色泡泡，将其颜色改为附近颜色最多的
        if cur_clr not in neib_clrs:
            distict_clr = list(set(neib_clrs))
            clr_cnt = [neib_clrs.count(distict_clr[i]) for i in range(len(distict_clr))]
            ind = clr_cnt.index(max(clr_cnt))
            oneline_chess[i] = distict_clr[ind]

    return oneline_chess


def random_fill_basic_ball(array_chess):
    '''
    以输入的二维矩阵为基础，随机填充彩色泡泡. 每次随机在矩阵中画一定长度的线
    直到没有位置可画.
    :param array_chess:
    :return:
    '''
    rows, cols = len(array_chess), BALL.BALLS_PER_ROW
    min_length = 3
    max_length = 15

    line_chess = util.array2oneline_list(array_chess)
    for i in range(rows*cols):
        rr, cc = int(i/BALL.BALLS_PER_ROW), int(i%BALL.BALLS_PER_ROW)

        # 从最下面第0层开始算，奇数行最后那个元素不管;
        if (rows-1-rr)%2!=0 and cc==BALL.BALLS_PER_ROW:
            continue

        # 如果已经有了颜色
        if line_chess[i] != BALL.ELEMENT_INIT:
            continue
        else:
            # 4种颜色
            clr = random.choice([1,2,3,4])
            # 连串的个数
            count = random.randint(min_length, max_length)
            line_chess[i] = clr
            while count-1>0:
                found, nr, nc = eo.random_next_empty_neib(line_chess, rr, cc)
                if found:
                    line_chess[nr*BALL.BALLS_PER_ROW+nc] = clr
                    count = count - 1
                else:
                    break

    line_chess = remove_single_ball(line_chess)
    return util.oneline_list2array(line_chess)
