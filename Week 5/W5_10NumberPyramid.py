"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def addition(limit):
    """This function will do something very coool"""
    for j in range(limit):
        for _ in range(((limit-1) * 3) - (3 * j)):
            print(end=" ")
        for i in range(j+1):
            print(("%02d" %(i+1)), end=" ")
        print()
addition(int(input()))
