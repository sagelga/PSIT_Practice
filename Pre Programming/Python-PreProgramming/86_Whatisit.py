"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    message_a = input()
    message_b = input()
    while message_b != message_a:
        message_b = input()
    print("This is it!", message_b)
major_branch()
