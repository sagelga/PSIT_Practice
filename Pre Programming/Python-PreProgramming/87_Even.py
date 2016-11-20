"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    count = 0
    maxim = int(input()) + 1
    while count != maxim:
        if count % 2 == 0:
            print(count)
            count += 1
        else:
            print("Odd")
            count += 1
major_branch()
