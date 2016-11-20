"""this is a docstring"""
def bounce():
    """this is a docstring"""
    num, count = float(input()), 0
    while True:
        num *= .6
        if num <= .01:
            return count
        count += 1
print(bounce())
