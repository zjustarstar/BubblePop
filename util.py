# 一些工具，用于矩阵和一维谜面的转换等

from PIL import Image, ImageDraw
import numpy as np
import ball_def as BALL


def array2oneline_list(chess):
    '''
    将每行11列的二维数组转为一维
    :param chess: 每行11列的二维数组
    :return: 平铺后的一维数组
    '''
    rows, cols = len(chess), BALL.BALLS_PER_ROW
    np_chess = np.array(chess)
    one_line_chess = np_chess.reshape(1, rows*cols)
    chess = one_line_chess.tolist()[0]
    return chess


def oneline_list2array(line_chess):
    '''
    将一维数组转化为每行为11列的二维数组
    :param line_chess: 一维数组
    :return: 转化为每行11列的二维数组
    '''
    rows = int(len(line_chess) / BALL.BALLS_PER_ROW)
    np_line = np.array(line_chess)
    arr_chess = np_line.reshape((rows, BALL.BALLS_PER_ROW))
    chess = arr_chess.tolist()

    return chess


def getBallColor(code):
    if code == BALL.ELEMENT_BLUE:
        return (0, 0, 255)
    elif code == BALL.ELEMENT_GREEN:
        return (0, 255, 0)
    elif code == BALL.ELEMENT_RED:
        return (255, 0, 0)
    elif code == BALL.ELEMENT_YELLOW:
        return (255, 255, 0)
    # elif code == BALL.EMPTY:
    #     return (0, 0, 0)
    else:
        return (125, 125, 125)


def chess2img(chess, name, savefile=''):
    '''
    根据二维的chess数据生成谜面的画面
    :param chess:二维数据
    :param name:如果不为空，则为要显示的窗口的名字
    :param savefile: 如果不为空，则保存为该文件名
    :return:无
    '''
    ball_d = 30  # 画出来的泡泡的直径
    rows, cols = len(chess), BALL.BALLS_PER_ROW

    img = Image.new('RGB', (cols*ball_d, rows*ball_d), 'lightgray')
    draw = ImageDraw.Draw(img)
    for r in range(rows):
        cc = chess[r]
        # 最底下是第0行
        y = (rows - 1 - r) * ball_d
        if r%2 == 0:
            margin = 0
            colsize = BALL.BALLS_PER_ROW
        else:
            margin = ball_d / 2
            colsize = BALL.BALLS_PER_ROW-1

        for i in range(colsize):
            x1 = i * ball_d + margin
            clr = getBallColor(cc[i])
            draw.ellipse(((x1, y), (x1 + ball_d, y + ball_d)), fill=clr, outline=clr, width=2)

    if len(name):
        img.show(name)
    if len(savefile):
        img.save(savefile)
