"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def addition(limit):
    """This function will do something very coool"""
    blank, current = (limit-1) * 3, 1
    for _ in range(limit):
        for _ in range(blank):
            print(end=" ")
        for i in range(current):
            print(("%02d" %(i+1)), end=" ")
        for i in range(current, 1, -1):
            print(("%02d" %(i-1)), end=" ")
        blank -= 3
        current += 1
        print()
addition(int(input()))
