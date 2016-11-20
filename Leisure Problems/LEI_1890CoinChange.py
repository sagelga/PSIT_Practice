"""this is a docstring"""
def coinchange():
    """this is a docstring"""
    num = int(input())
    total = 0
    coin = [25, 10, 5, 1]
    for i in coin:
        total += num // i
        num -= (num // i) * i
    print(total)
coinchange()
