"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    counter = 0
    number = float(input())
    while number <= 100 and number != 0:
        counter += number
        number = float(input())
    print(int(counter))
major_branch()
