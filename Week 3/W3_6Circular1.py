"""This program will check is either the mosquito is in range"""
import math
def repellant():
    """The function will check is either the mosquito is in range."""
    (you_x, you_y, radius) = (float(input()), float(input()), float(input()))
    (me_x, me_y) = (float(input()), float(input()))
    if math.sqrt(((you_x - me_x) ** 2) + ((you_y - me_y)) ** 2) <= radius:
        print("Yes")
    else:
        print("No")
repellant()
