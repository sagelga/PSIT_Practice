"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print out the number exponent by 2
"""
def adding(limit):
    """This function will print out the number exponent by 2"""
    for i in range(1, limit):
        print(i**2, end=" ")

adding(int(input()))
