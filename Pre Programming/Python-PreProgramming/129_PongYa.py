"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    number = input()
    if number.endswith("3"):
        print("Pong")
    else:
        number = int(number)
        if number % 3 == 0:
            print("Pong")
        else:
            print(number)
major_branch()
