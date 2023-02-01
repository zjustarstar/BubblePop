# chess的第0行，对应谜面的最底层
import ball_def as BALL
import random
import util
import element_operation as eo
import chess_operation as co


# 随机往上挑选空的相邻元素，组成整个谜面最左边的空泡泡区域
# 二维矩阵的坐标，最上面一行为0.
def random_next_empty_neib(line_num, col_index):
    res_row_num = line_num - 1
    # 偶数行
    if line_num % 2 == 0:
        res_col_num = col_index + random.choice([-1, 0])
        # 考虑最左边的元素
        res_col_num = max(0, res_col_num)
    else:
        res_col_num = col_index + random.choice([1, 0])

    return res_row_num, res_col_num


def setEmptyMargin(chess):
    rows, cols = len(chess), BALL.BALLS_PER_ROW

    max_margin_length = 3   # 边界最长不能超过这个
    empty_index = random.randint(0, max_margin_length)
    # 从最底下开始设置空的泡泡
    for r in range(rows-1, -1, -1):
        line = chess[r]
        line[0:empty_index] = [BALL.EMPTY] * empty_index
        _, empty_index = random_next_empty_neib(r, empty_index)
        if empty_index>max_margin_length:
            empty_index = max_margin_length

    return chess


rows = 80
stru_symmetry = True
chess = [[BALL.ELEMENT_INIT for i in range(11)] for i in range(rows)]

# chess = co.mirrorX(setEmptyMargin(chess))
# chess2img(chess, "chess1")

newchess = co.random_fill_basic_ball(chess)
if stru_symmetry:
    newchess = co.mirrorX(newchess)

util.chess2img(newchess, "chess2", "bubble.jpg")

print(chess)
