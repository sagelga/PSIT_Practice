"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    message = input()
    lengths = len(message)
    count = 0
    if message[0].isdigit() or (message[index - 1] == 0 and message[index].isdigit()):
        modes = 0
    else:
        modes = 1
    while count != lengths:
        if message[count] == "0":
            print("\n")
            count += 1
        if message[count].isdigit() and modes == 0:
            print(" ")
            modes = 1
            count += 1
        if message[count].isdigit() and modes == 1:
            print(message[count - 1] * int(message[count]))
            modes = 0
            count += 1
        else:
            count += 1
major_branch()
