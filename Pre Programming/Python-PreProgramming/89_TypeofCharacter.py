"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    message = input()
    count = 0
    for count in range(0, len(message)):
        if message[count].islower():
            print(message[count], "is lowercase letter")
            continue
        if message[count].isupper():
            print(message[count], "is uppercase letter")
            continue
        else:
            print(message[count], "is number")
            continue
    count += 1
major_branch()
