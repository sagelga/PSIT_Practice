"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    listings = []
    counter = 0
    limits = int(input())
    while limits != counter:
        message = input()
        listings.append(message)
        counter += 1
    print(listings)
major_branch()
