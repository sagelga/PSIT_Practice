"""
This program will be happy
Part of the Preprogramming Course 2016
"""
def major_branch():
    """Program will revert | print out text multiple times"""
    message = input()
    if message[-1].isdigit:
        if len(message) == 1:
            print(message + message) * 15)
        else:
            print(message[-1] * 15)
    else:
        if message[0] == "A" or message[0] == "a":
            print(message[::-1] * 69)
        if message[0] == "E" or message[0] == "e":
            print(message[::-1] * 69)
        if message[0] == "I" or message[0] == "i":
            print(message[::-1] * 69)
        if message[0] == "O" or message[0] == "o":
            print(message[::-1] * 69)
        if message[0] == "U" or message[0] == "u":
            print(message[::-1] * 69)
        else:
            print(message * 96)



    """This is the main fuction. It will do everything."""
major_branch()
