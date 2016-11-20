"""This program will find the peaked data, without using some function."""
def peaked_finder():
    """The function will try to find out the data, by checking the number nearby."""
    text_1 = int(input())
    text_2 = int(input())
    text_3 = int(input())
    text_4 = int(input())
    text_5 = int(input())
    text_6 = int(input())
    text_7 = int(input())
    text_8 = int(input())
    if text_1 > text_2:
        (text_1, text_2) = (text_2, text_1)
    if text_2 > text_3:
        (text_2, text_3) = (text_3, text_2)
    if text_3 > text_4:
        (text_3, text_4) = (text_4, text_3)
    if text_4 > text_5:
        (text_4, text_5) = (text_5, text_4)
    if text_5 > text_6:
        (text_5, text_6) = (text_6, text_5)
    if text_6 > text_7:
        (text_6, text_7) = (text_7, text_6)
    if text_7 > text_8:
        (text_7, text_8) = (text_8, text_7)
    print(text_8)
peaked_finder()
