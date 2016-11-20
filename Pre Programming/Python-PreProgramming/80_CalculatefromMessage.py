"""
This program will calculate and sort out the minimum and maximum
Part of the Preprogramming Course 2016
"""
def calculate_message():
    """Max values and min values will be exponented"""
    msg_a = input()
    msg_b = input()
    length_a = len(msg_a)
    length_b = len(msg_b)
    if (length_a % 2) == 0 and (length_b % 2) == 0:
        print(max((length_a ** 2), (length_b ** 2)))
        print(min((length_a ** 2), (length_b ** 2)))
    elif (length_a % 2) == 1 and (length_b % 2) == 1:
        print(max((length_a ** 3), (length_b ** 3)))
        print(min((length_a ** 3), (length_b ** 3)))
    else:
        print((max((length_a ** 4), (length_b ** 4))) - (min((length_a ** 4), (length_b ** 4))))
calculate_message()
