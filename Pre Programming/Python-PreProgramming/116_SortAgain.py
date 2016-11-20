"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    counter = 0
    limits = int(input())
    listings = []
    while counter != limits:
        listings.append(float(input()))
        counter += 1
    listings.sort()
    counter = 0
    while counter != limits:
        number = listings[counter]
        if number % 1 == 0:
            print(int(number), end=" ")
        else:
            print(number, end=" ")
        counter += 1
major_branch()
