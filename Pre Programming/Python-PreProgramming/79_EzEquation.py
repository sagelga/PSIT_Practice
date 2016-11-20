"""
This program will ask for input > run code & algorithm > output
Part of the Preprogramming Course 2016
"""
import math
def equations():
    """This is the main fuction. It will do everything."""
    path_a = math.sqrt(3 * 1.45)
    path_b = (85/5)
    path_c = (math.e * 95.632)
    path_d = (math.pi ** 3 ** 2) + (math.pi + math.e)
    path_a = path_a / path_b
    path_c = path_c / path_d
    print(int(path_a - path_c * (2 ** 5)))
equations()
