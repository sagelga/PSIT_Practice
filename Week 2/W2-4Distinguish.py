"""This program will testing out, is the number excede 180"""
def edge_calculator():
    """The function will test the vadiation of the input. Then print out result"""
    text = int(input())
    if text > 180:
        print("You're hit the door edge.")
    if text <= 180:
        print("Nothing happens.")
edge_calculator()
