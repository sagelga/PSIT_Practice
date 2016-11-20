"""This program will answer the problem by solving simple mathematics equation"""
import math
def trigonometrys():
    """This function will answer the problem by solving simple mathematics equation"""
    top_calc = math.sin(math.radians(90)) + pow(math.sin(math.radians(60)), 2)
    bottom_calc = math.cos(math.radians(245 * 245)) + math.cos(math.radians(45 + 135))
    print(top_calc / bottom_calc)
    #
    top_calc = math.factorial(16) * math.factorial(4)
    bottom_calc = math.factorial(8)
    print(top_calc / bottom_calc)
    #
    top_calc = 15  + 25
    bottom_calc = math.sqrt(pow(((25 - 12)), 2) + pow(((12 - 15)), 2))
    print(top_calc / bottom_calc)
    #
    print(math.log10(math.pow(1234, 4)))
    #
    top_calc = math.log(4234, 5) + math.log(8191, 2) + (71 * (math.log10(156154)))
    bottom_calc = math.log(777, 7) - math.log(888, 8) - math.log(999, 9)
    print(top_calc / bottom_calc)
trigonometrys()
