"""
This program will ask input > run code & algorithm > output
Part of the Preprogramming Course 2016
"""
def text_swapcase():
    """This is the main fuction. It will do everything."""
    message_a = input()
    message_b = input()
    if message_a.islower() and message_b.islower():
        print(message_a.upper())
        print(message_b.upper())
    elif message_a.isupper() and message_b.isupper():
        print(message_a.lower())
        print(message_b.lower())
    else:
        print("Python is so Ez")
text_swapcase()
