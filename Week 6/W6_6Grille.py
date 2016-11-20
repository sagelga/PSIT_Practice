"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print in pattern
"""
def addition(y_axis, x_axis):
    """This function will print in patterns"""
    if x_axis <= 1:
        for _ in range(y_axis):
            print("*" * x_axis)
        return
    for i in range(1, y_axis+1):
        if i % 2:
            print("* " * ((x_axis + 1) // 2))
        else:
            print(" *" * ((x_axis) // 2))

addition(int(float(input())), int(float(input())))
