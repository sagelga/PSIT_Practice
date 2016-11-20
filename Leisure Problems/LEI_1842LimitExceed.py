"""this is a docstring"""
def limitexceed():
    """this is a docstring"""
    total = 0
    while True:
        total += int(input())
        if total > 1024:
            return total

print(limitexceed())
