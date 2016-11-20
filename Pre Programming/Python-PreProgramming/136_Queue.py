"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    message = []
    limits = int(input())
    for _ in range(limits):
        message.append(input())
    suspended = int(input()) - 1
    print(' '.join(message))
    laters = message[suspended]
    message[suspended] = "Toilet"
    print(' '.join(message))
    del message[suspended]
    if limits != 1:
        print((' '.join(message)), "-->" + laters, "I'm back")
    else:
        print("-->" + laters, "I'm back")
major_branch()
