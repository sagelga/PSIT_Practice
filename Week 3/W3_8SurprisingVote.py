"""This program will check is either the vote is way too down or not"""
import math
def voters():
    """The function will check is either the vote is surprise or not"""
    (total, maxim) = (float(input()), float(input()))
    if maxim * 2 <= total:
        middle = maxim
    else:
        middle = math.ceil((total - maxim) / 2)
    if maxim - (total - maxim - middle) > 2:
        print("Surprising")
    else:
        print("Not surprising")
voters()
