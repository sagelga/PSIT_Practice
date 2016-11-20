"""This program will try to distribute pizza slice into the appropriate box size"""
import math
def pizza_distribute():
    """This thing will distribute pizza and output the appropriate box size"""
    count = int(input())
    large_pizza = math.floor(count / 12)
    count -= (large_pizza * 12)
    medium_pizza = math.floor(count / 9)
    count -= (medium_pizza * 9)
    small_pizza = math.ceil(count / 6)
    print(large_pizza, "/", medium_pizza, "/", small_pizza)
pizza_distribute()
