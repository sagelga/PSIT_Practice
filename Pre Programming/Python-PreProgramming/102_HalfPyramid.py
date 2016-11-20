"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    counter = int(input()) + 1
    for i in range(1, counter):
        print(i * "*")
major_branch()
