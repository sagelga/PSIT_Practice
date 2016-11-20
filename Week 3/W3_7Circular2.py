"""This program will find out that the circle is cut or not"""
import math
def circlecut():
    """The fuction will find out is the circle is cut or not"""
    (you_x, you_y, you_range) = (float(input()), float(input()), float(input()))
    (me_x, me_y, me_range) = (float(input()), float(input()), float(input()))
    if math.sqrt((you_x-me_x)**2 + (you_y-me_y)**2) < (you_range+me_range):
        print("Yes")
    else:
        print("No")
circlecut()
