"""this is a docstring"""
def challenge():
    """this is a docstring"""
    text = input()
    pts_a, pts_b = 0, 0
    for i in range(0, len(text), 2):
        user_a = text[i]
        user_b = text[i + 1]
        if user_a == "R" and user_b == "S":
            pts_a += 1
        elif user_a == "R" and user_b == "P":
            pts_b += 1
        elif user_a == "P" and user_b == "R":
            pts_a += 1
        elif user_a == "P" and user_b == "S":
            pts_b += 1
        elif user_a == "S" and user_b == "R":
            pts_b += 1
        elif user_a == "S" and user_b == "P":
            pts_a += 1
    if pts_a > pts_b:
        print("A win", "%s" %pts_a + "-" + "%s" %pts_b)
    elif pts_a < pts_b:
        print("B win", "%s" %pts_b + "-" + "%s" %pts_a)
    else:
        print("DRAW", pts_a)
challenge()
