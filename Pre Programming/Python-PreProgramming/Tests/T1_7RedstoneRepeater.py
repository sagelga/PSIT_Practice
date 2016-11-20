"""This program will"""
def fname():
    """This thing will"""
    length = int(input())
    if length <= 8:
        print("%" * length)
    else:
        print(("%" * 8) + "-" * (length - 8))
fname()
