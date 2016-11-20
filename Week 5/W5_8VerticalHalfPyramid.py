"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def addition(limit):
    """This function will do something very coool"""
    for i in range(limit):
        for j in range(i+1):
            print(j+1, end=" ")
        print()
addition(int(input()))
