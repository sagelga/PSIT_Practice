"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def addition(limit):
    """This function will do something very coool"""
    blank, current = (limit-1) * 3, 1
    for _ in range(limit):
        space(blank)
        border(current)
        diamond_core(current)
        blank, current = (blank - 3), (current + 1)
        print()
    blank, current = 3, (current - 1)
    for _ in range(limit):
        space(blank)
        blank, current = (blank + 3), (current - 1)
        border(current)
        diamond_core(current)
        print()

def space(blank):
    """This function will do something very coool"""
    for _ in range(blank):
        print(end=" ")

def border(current):
    """This function will do something very coool"""
    for i in range(current):
        print(("%02d" %(i+1)), end=" ")

def diamond_core(current):
    """This function will do something very coool"""
    for i in range(current, 1, -1):
        print(("%02d" %(i-1)), end=" ")

addition(int(input()))
