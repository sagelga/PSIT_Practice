"""THis is a docstring"""
def quadrant():
    """This is a docstring"""
    num1, num2 = int(input()), int(input())
    if num1 > 0 and num2 > 0:
        print("Q1")
    if num1 > 0 and num2 < 0:
        print("Q4")
    if num1 < 0 and num2 > 0:
        print("Q2")
    if num1 < 0 and num2 < 0:
        print("Q3")
    if num1 == 0 and num2 != 0:
        print("Y")
    if num2 == 0 and num1 != 0:
        print("X")
    if num1 == 0 and num2 == 0:
        print("O")
quadrant()
