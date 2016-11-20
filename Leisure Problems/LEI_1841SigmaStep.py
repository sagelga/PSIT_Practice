"""this is a docstring"""
def sigmastep():
    """this is a docstring"""
    start, stop, step = int(input()), int(input()), int(input())
    if start > stop:
        return "error"
    total = 0
    for i in range(start, stop, step):
        total += i
    return total
print(sigmastep())
