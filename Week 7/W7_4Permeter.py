"""Pair Programming Week 7 by K. Srisuntiroj ID0022
The program will calculate the radiance of the input given"""
import math
def perimeter(num, radiac):
    """This will calculate the radiance of the input given"""
    perimeter = (2 * num * radiac * float("%.8f" % (math.sin(math.pi/num))))
    print("%.1f" % perimeter)
perimeter(int(input()), float(input()))
