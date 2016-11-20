"""Pair Programming by Kunanon S. 59070022
This program will print out the text in a good look"""
def ascending(text):
    """This function ascend the text"""
    for i in range(1, len(text)):
        blank = len(text) - i
        print(" "*blank + text[:i])

def descending(text):
    """This function ascend the text"""
    for i in range(1, len(text)):
        blank = len(text) - i
        print(text[i:] + " "*blank)

def calling(text):
    """This function calls another function x times"""
    ascending(text)
    print(text)
    descending(text)

calling(input())
