"""This program will ask input then, run the program, later then print out the results"""
def mutiply_table():
    """This is the main fuction. It will do everything."""
    number = int(input())
    counter = 0
    while counter != 12:
        counter += 1
        print(number, "X", "%-2d" %counter, "=", (number * counter))
mutiply_table()
