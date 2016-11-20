"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will add _ after each number count
"""
def splitting(limit):
    """This program will split the number"""
    for i in range(limit):
        if i != limit-1:
            print(i+1, end="_")
        else:
            print(i+1)
splitting(int(input()))
