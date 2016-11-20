"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    accu_balance = 0
    total = 0
    for _ in range(int(input())):
        message = input()
        message.split(" ")
        total = int(message[1]) * int(message[2])
        print(message, total)
        accu_balance += total
    print(accu_balance)
major_branch()
