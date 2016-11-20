"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    message = input()
    count = 0
    message.split(" ")
    sorted(message)
    print(message)
    while message[0] != 1:
        sorted(message)
        for i in range(1, 3):
            message[i] = int(message[i]) - 1
        print(message)
        count += 1
    print(message)
major_branch()
