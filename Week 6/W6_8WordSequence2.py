"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def lines(txt_1, txt_2):
    """This function will increase the word length every time"""
    maxim = max(len(txt_1), len(txt_2))
    for i in range(maxim+1):
        print(txt_2[0:i], end="")
        print(txt_1[i:maxim], end="")
        print()
lines(input(), input())
