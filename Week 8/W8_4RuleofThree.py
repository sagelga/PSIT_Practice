"""This prorgam will calculate the cheapest values"""
def calculate(min_price, min_weight, min_values):
    """This prorgam will calculate the cheapest values"""
    for _ in range(int(input())):
        price, weight = float(input()), float(input())
        if (price / weight) < min_values:
            min_price, min_weight, min_values = price, weight, (price / weight)
        if ((price / weight) == min_values) and (price < min_price):
            min_price, min_weight, min_values = price, weight, (price / weight)
    print("%.2f %.2f" %(min_price, min_weight))

calculate(0, 0, 999999999999)
