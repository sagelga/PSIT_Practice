"""This program will run wheaver the input is in range of 0-120 and change back to grades"""
def inandout():
    """It is doing some nested if-else relationship,
    to find the real grades that have been calculated."""
    number = int(input())
    if number > 0:
        counter = 1
        print(1)
        while counter != number:
            counter += 1
            print(counter)
        while counter != 1:
            counter -= 1
            print(counter)
    else:
        counter = 1
        print(1)
        while counter != number:
            counter -= 1
            print(counter)
        while counter != 1:
            counter += 1
            print(counter)
inandout()
