"""
This program will try to compare between length of the string 2 times.
Part of the Preprogramming Course 2016
"""
def text_comparator():
    """This will identify the length to the string given 2 input
    and output depending on their correctness"""
    text_a = input()
    text_b = input()
    length_a = int(input())
    length_b = int(input())
    if len(text_a) == length_a and len(text_b) == length_b:
        print("Banana Bird")
    else:
        if (text_b.endswith("o") or text_b.endswith("O")) and text_a.isalpha():
            print("Lnwza007")
        else:
            print("eieiii")
text_comparator()
