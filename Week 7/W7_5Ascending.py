"""Pair Programming Week 7 by K. Srisuntiroj ID0022
The program will sort out the 5 numbers given ascendingly"""
def ascendingly(num1, num2, num3, num4, num5):
    """This will sort out the 5 numbers given ascendingly"""
    for _ in range(5):
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 > num3:
            num2, num3 = num3, num2
        if num3 > num4:
            num3, num4 = num4, num3
        if num4 > num5:
            num4, num5 = num5, num4
    print(num1)
    print(num2)
    print(num3)
    print(num4)
    print(num5)

ascendingly(int(input()), int(input()), int(input()), int(input()), int(input()))
