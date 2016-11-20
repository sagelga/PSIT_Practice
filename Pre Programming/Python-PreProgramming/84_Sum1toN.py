"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    num = int(input())
    total = 0
    for _ in range(0, num + 1):
        total = total + _
    print(total)
major_branch()
