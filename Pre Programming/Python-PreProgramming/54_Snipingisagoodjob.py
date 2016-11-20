"""
This program will ask for input > run code & algorithm > output
Part of the Preprogramming Course 2016
"""
def major_branch():
    """This is the main fuction. It will do everything."""
    comments = input()
    per_a = float(input())
    per_b = float(input())
    per_c = float(input())
    per_d = float(input())
    per_e = float(input())
    per_f = float(input())
    per_g = float(input())
    print("Min Headshot rate :", "%.2f" %((min(per_a, per_b, per_c, per_d, per_e, per_f, per_g)), end="%"))
    print("Max Headshot rate :", "%.2f" %((max(per_a, per_b, per_c, per_d, per_e, per_f, per_g)), end="%"))
    print("Med Headshot rate :", "%.2f" %((per_a + per_b + per_c + per_d + per_e + per_f + per_g) / 7), end="%")
    print("You know, " + comments + ". sniping is a good job!")
major_branch()
