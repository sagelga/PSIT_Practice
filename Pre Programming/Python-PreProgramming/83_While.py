"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    num = int(input())
    num2 = int(input())
    counter = 0
    while num <= num2:
        num += 1
        counter += 1
    print(counter)
major_branch()
