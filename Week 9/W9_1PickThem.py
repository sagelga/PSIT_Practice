"""This is preprogramming by Kunanon S."""
import json
def caller():
    """This function will do something"""
    line, trigger = json.loads(input()), True
    for i in line:
        if i % 2 == 0:
            print(i)
            trigger = False
    if trigger:
        print("Nope")

caller()
