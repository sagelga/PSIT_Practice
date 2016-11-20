"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    ampare = float(input())
    message = input()
    message = message.replace("[", "")
    message = message.replace("]", "")
    message = message.split(", ")
    for i in range(len(message)):
        message[i] = float(message[i]) * ampare
    print(message)
major_branch()
