"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    message = input()
    length = len(message)
    counter = 0
    while counter != length:
        print(message[counter])
        counter += 1
major_branch()
