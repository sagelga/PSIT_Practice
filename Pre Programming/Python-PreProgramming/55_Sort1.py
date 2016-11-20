"""This program will do something with the numbers, with the exceptions of conditions"""
def major_branch():
    """This is the main fuction. It will do everything."""
    var_a = int(input())
    var_b = int(input())
    var_c = int(input())
    minimum = min(var_a, var_b, var_c)
    maximum = max(var_a, var_b, var_c)
    medians = (var_a + var_b + var_c) - (minimum + maximum)
    print(minimum)
    print(medians)
    print(maximum)
major_branch()
