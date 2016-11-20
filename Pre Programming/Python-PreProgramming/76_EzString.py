"""
This program will ask for input > run code & algorithm > output
Part of the Preprogramming Course 2016
"""
def easy_string():
    """This is the main fuction. It will do everything."""
    message = input()
    frequency = int(input())
    length = len(message)
    print(((message + " ") * frequency))
    print(message + " " + (str(frequency) * frequency))
    print(message + " " + message[::-1])
    if length >= 3:
        print(message[:-4:-1])
    else:
        print(message[::-1])
easy_string()
