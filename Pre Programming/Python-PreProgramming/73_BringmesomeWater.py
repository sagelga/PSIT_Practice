"""This program will ask for input > run code & algorithm > output"""
import math
def major_branch():
    """This is the main fuction. It will do everything."""
    amount = int(input())
    counter = 0
    if amount < 10:
        big_water = amount // 5
        amount -= big_water * 5
        small_water = math.ceil(amount / 2)
    else:
        big_water = amount // 5
        if amount % 2 == 0 or amount % 10 == 7 or amount % 10 == 9:
            amount -= big_water * 5
            small_water = amount / 2
        else:
            while amount % 2 == 1:
                big_water -= 1
                amount += 5
                counter += 5
            amount -= big_water * 5
            amount -= counter
            small_water = int(amount / 2)
    print(big_water)
    print(small_water)
major_branch()
