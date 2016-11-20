"""This program will ask input then, run the program, later then print out the results"""
def odd_and_even():
    """This is the main fuction. It will do everything."""
    message = int(input())
    while message != 1:
        if message % 2 == 0:
            print(int(message), end=" ")
            message /= 2
        else:
            print(int(message), end=" ")
            message += 1
    print("1")
odd_and_even()
