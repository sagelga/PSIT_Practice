"""this is a docstring"""
import random
def letter_mining():
    """This is a docstring"""
    text = input()
    letters = []
    combinations = []
    for i in text:
        letters.append(i)
    for _ in range(5 ** len(text)):
        random.shuffle(letters)
        new = ""
        for i in letters:
            new += i
        combinations.append(new)
    for _ in range(2 ** len(text)):
        combinations = [value for value in combinations if value != text]
        text = input()

letter_mining()
