"""this is a docstring"""
def compound():
    """this is a docstring"""
    money, interest, year = int(input()), float(input()) / 100, int(input())
    for _ in range(year):
        money += money * interest
    print("%.2f" %money)
compound()
