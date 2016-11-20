"""This is a docstring"""
def sandwitch(length, text1, text2):
    """This is also a docstring"""
    print(text1 + " " * (length-len(text1)-len(text2))+text2)
sandwitch(int(input()), input(), input())
