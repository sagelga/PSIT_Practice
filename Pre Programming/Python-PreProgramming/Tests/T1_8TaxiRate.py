"""This program will"""
import math
def fname():
    """This thing will"""
    length = int(input())
    time = int(input())
    price = math.ceil(time / 60) * 1.5
    if length >= 0:
        price += 50
        length -= 1
    if length >= 1:
        price += (5 * length)
        length -= 9
    if length >= 1:
        price += (2.5 * length)
        length -= 10
    if length >= 1:
        price += (2.5 * length)
        length -= 20
    if length >= 1:
        price += (2.5 * length)
        length -= 25
    if length >= 1:
        price += (2.5 * length)
    print(math.ceil(price))
fname()
