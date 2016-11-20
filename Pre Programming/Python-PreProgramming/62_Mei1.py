"""
This program will ask for input > run code & algorithm > output
Part of the Preprogramming Course 2016
"""
def solokill():
    """This is the main fuction. It will do everything."""
    damage = int(input())
    health = int(input())
    if damage >= 80:
        damage += 75
        if damage >= health:
            print("Solo_Kill")
        else:
            print(damage)
    else:
        print(damage)
solokill()
