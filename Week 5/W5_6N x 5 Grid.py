"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def addition(limit):
    """This function will do something very coool"""
    for i in range(limit):
        for j in range(limit):
            count = ((i*limit)+1) + j
            print(count, end=" ")
        print()
addition(int(input()))
