"""this is docstring"""
def marcaron():
    """this is docstring"""
    number = int(input())
    lrg, med, sml = 0, 0, 0
    while (12 > number >= 24) and (number / 24) > 0:
        lrg += 1
        number -= 24
    while (6 > number >= 12) and (number / 12) > 0:
        med += 1
        number -= 12
    while (number >= 6) and (number / 6) > 0:
        sml += 1
        number -= 6
    print(sml, med, lrg, end="\n")
marcaron()
