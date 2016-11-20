"""This is function"""
def inversions():
    """This is function"""
    trigger = False
    text = input()
    for i in text:
        if i == "1" and trigger:
            print("0", end="")
        elif i == "0":
            print("1", end="")
            trigger = True
inversions()
