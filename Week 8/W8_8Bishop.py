def bishop():
    """This thing will consider the validity of the alignment"""
    board_x, board_y = int(input()), int(input())
    bi_x, bi_y = int(input()), int(input())
    ob_x, ob_y, enemy = int(input()), int(input()), int(input())
    tg_x, tg_y = int(input()), int(input())
    x_diff = bi_x - tg_x
    y_diff = bi_y - tg_y
    sign_x, sign_y = 0, 0
    if x_diff > 0:
        sign_x = 1
    if y_diff > 0:
        sign_y = 1
    if bi_x > board_x or ob_x > board_x or tg_x > board_x:
        return 0
    if bi_y > board_y or ob_y > board_y or tg_y > board_y:
        return 0
    if abs(x_diff) == abs(y_diff):
        signs_x, signs_y = 0, 0
        x_dif = bi_x - ob_x
        y_dif = bi_y - ob_y
        if x_dif > 0:
            sign_x = 1
        if y_dif > 0:
            sign_y = 1
        if x_diff == y_diff:
            return 0
        elif ob_x == tg_x and ob_y == tg_y and enemy == 0:
            return 1
    return 0

def caller():
    """Print the text, relevant to the answer of the bishop function"""
    if bishop():
        print("Yes")
    else:
        print("No")

caller()

