"""this is a docstring"""
def vowel():
    """this is a docstring"""
    listing = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in input():
        if i not in listing:
            print(i, end="")
vowel()
