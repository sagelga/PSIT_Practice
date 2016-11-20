"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def addition(limit):
    """This function will do something very coool"""
    for _ in range(limit):
        for j in range(limit, limit-7, -1):
            if j > 0:
                print(j, end=" ")
            continue
        limit -= 7
        print()
addition(int(input()))
