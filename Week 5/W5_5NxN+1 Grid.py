"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def addition(limit):
    """This function will do something very coool"""
    base = 2
    for _ in range(limit):
        for i in range(base, base+limit):
            print(i, end=" ")
        print(end="\n")
        base += 1
addition(int(input()))
