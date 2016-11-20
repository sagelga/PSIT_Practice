"""this is some text"""
def checker(text, number):
    """this is some text"""
    for i in text:
        if i != number:
            print("no")
            return
    print("yes")
checker(input(), input())
