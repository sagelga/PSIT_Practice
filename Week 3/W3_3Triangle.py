"""This program will arrange item in order in ascending or descending"""
def pytagorus():
    """This will find out the input and sent the results to coorespond fuction"""
    side_a = float(input())
    side_b = float(input())
    side_c = float(input())
    for _ in range(2):
        if side_a > side_b:
            (side_a, side_b) = (side_b, side_a)
        if side_b > side_c:
            (side_b, side_c) = (side_c, side_b)
    side_a **= 2
    side_b **= 2
    side_c **= 2
    if side_c - side_a - side_b == 0:
        print("Yes")
    elif side_c - .01 <= side_a + side_b <= side_c + .01:
        print("Yes")
    else:
        print("No")
pytagorus()
