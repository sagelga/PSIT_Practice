"""this is a thing"""
def directions():
    """this is a text"""
    up_direction = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
    down_direction = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
    left_direction = ["  *  ", " *   ", "*****", " *   ", "  *  "]
    right_direction = ["  *  ", "   * ", "*****", "   * ", "  *  "]
    text = input()
    for i in range(5):
        for j in text:
            if j == "U":
                print(up_direction[i], end=" ")
            elif j == "D":
                print(down_direction[i], end=" ")
            elif j == "L":
                print(left_direction[i], end=" ")
            elif j == "R":
                print(right_direction[i], end=" ")
        print()
directions()
