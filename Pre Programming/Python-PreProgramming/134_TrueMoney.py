"""This program will ask input then, run the program, later then print out the results"""
import math
def major_branch():
    """This is the main fuction. It will do everything."""
    small = 0
    medium = 0
    large = 0
    for _ in range(int(input())):
        message = input()
        message = message.split()
        small += int(message[0])
        medium += int(message[1])
        large += int(message[2])
    if small >= 1000:
        small *= 0.85
    else:
        if small >= 500:
            small *= .9
        else:
            if small >= 100:
                small *= .95
    if medium >= 1000:
        medium *= .85
    else:
        if medium >= 500:
            medium *= .9
        else:
            if medium >= 100:
                medium *= .95
    if large >= 1000:
        large *= .85
    else:
        if large >= 500:
            large *= .9
        else:
            if large >= 100:
                large *= .95
    print("TrueMoney : 150 =", math.ceil(small * 150))
    print("TrueMoney : 300 =", math.ceil(medium * 300))
    print("TrueMoney : 1000 =", math.ceil(large * 1000))
major_branch()
