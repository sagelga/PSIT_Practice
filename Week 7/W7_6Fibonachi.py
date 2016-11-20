"""Pair Programming Week 7 by K. Srisuntiroj ID0022
The program will calculate the Finonachi"""
def fibonachi(num, first, second):
    """This function will calculate the Finonachi"""
    for _ in range(num - 1):
        first, second = (first + second), first
    if num <= 1:
        current = num
    print(current)

fibonachi(int(input()), 1, 0)
