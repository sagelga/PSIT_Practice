"""
This program will ask for input > run code & algorithm > output
In this case given branched ASCII
"""
def major_branch():
    """This is the main fuction. It will do everything. Type in 2 input | 4 output"""
    var_a = input()
    var_b = input()
    num_a = int(var_a[:1])
    num_b = int(var_a[:-1])
    num_c = int(var_b[:1])
    num_d = int(var_b[:-1])
    max_num = int(max(num_a, num_b))
    min_num = int(min(num_c, num_d))
    print("Max ASCII Number Is:", max_num)
    print("Max ASCII Number Character Is:", chr(max_num))
    print("Min ASCII Number Is:", min_num)
    print("Min ASCII Number Character Is:", chr(min_num))
major_branch()
