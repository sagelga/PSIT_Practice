"""
This program will ask for input > run code & algorithm > output
Part of the Preprogramming Course 2016
"""
def major_branch():
    """This is the main fuction. It will do everything."""
    var_a = input()
    code = chr(int(input())) + chr(int(input()))
    var_a += var_a.count(code) * "HELLO"
    var_a.replace("%s" %code, "@")
    print(var_a)
major_branch()
