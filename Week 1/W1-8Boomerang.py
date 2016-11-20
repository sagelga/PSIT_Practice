"""Acquire the total of 3 inputs, runs through the equation, then print answer"""
def equationline():
    """Function will acquire inputs and doing equations"""
    var_x = int(input())
    var_y = int(input())
    var_z = int(input())
    print(var_x + 1)
    print((7 * (var_y ** 3)) + (2 * (var_y ** 2)) - (31 * var_y) + 1)
    print(-1 * var_z)
    print((var_x + var_y) * (var_x - var_y))
    print((var_y - (((var_y ** 2) - 4 * var_x * var_z) ** .5)) / (2 * var_x))
equationline()
