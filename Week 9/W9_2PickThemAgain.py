"""This is preprogramming by Kunanon S."""
def caller():
    """This function will do something"""
    line, trigger = input(), True
    line = line.split()
    for i in reversed(line):
        if (int(i) % 3 == 0) or (int(i) % 5 == 0):
            print(i)
            trigger = False
    if trigger:
        print("Nope")

caller()
