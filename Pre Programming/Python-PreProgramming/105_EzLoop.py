"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    total = int(input())
    counter = 0
    while counter != total:
        message = input()
        counter += 1
        print("input", counter, "is :", message)
major_branch()
