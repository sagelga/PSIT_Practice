"""this is text"""
def triangle():
    """this is text"""
    num1, num2 = int(input()) ** 2, int(input()) ** 2
    num3 = (num1 + num2) ** (1/2)
    if num3 == int(num3):
        print(int(num3))
    else:
        print("%.4f" %num3)
triangle()