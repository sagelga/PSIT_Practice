"""
This program will ask for input > run code & algorithm > output
Part of the Preprogramming Course 2016
"""
def take_easy():
    """This is the main fuction. It will do everything."""
    length = int(input())
    message = input()
    if length >= len(message):
        print("||||||" + "%.5s" %message + "||||||")
    else:
        print("           -----")
        print("-|-|-|-|-|-----" + "%.4s" %message + ")))")
        print("           -----")
take_easy()
