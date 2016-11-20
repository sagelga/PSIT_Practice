"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def lines(limit):
    """This function will increase the word length every time"""
    for i in range(len(limit)):
        print(limit[:i+1])
lines(input())
