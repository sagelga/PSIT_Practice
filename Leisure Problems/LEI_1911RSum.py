"""this is a docstring"""
def summation():
    """this is docstring"""
    num, total = int(input()), 0
    if num < 1:
        for i in range(1, num-1, -1):
            total += i
    else:
        for i in range(1, num+1):
            total += i
    print(total)
summation()
