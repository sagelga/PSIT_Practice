"""
This program will ask for input > run code & algorithm > output
Part of the Preprogramming Course 2016
"""
def major_branch():
    var_a = int(input())
    var_b = int(input())
    var_c = int(input())
    minim = min(var_a, var_b, var_c)
    maxim = max(var_a, var_b, var_c)
    median = var_a + var_b + var_c - maxim - minim
    if (minim ** 2) + (median ** 2) == (maxim ** 2 ):
        print("No")
    else:
        print("Yes")
    """This is the main fuction. It will do everything."""
major_branch()
