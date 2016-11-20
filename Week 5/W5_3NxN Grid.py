"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print out the number squares of input in size
"""
def adding(limit):
    """This function will loop the lines and print out the numbers"""
    for _ in range(limit):
        for j in range(limit):
            print(j+1, end=" ")
        print()
adding(int(input()))
