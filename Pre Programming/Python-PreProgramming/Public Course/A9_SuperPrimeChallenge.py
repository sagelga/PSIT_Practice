"""This program will run wheaver the input is in range of 0-120 and change back to grades"""
def grade():
    """It is doing some nested if-else relationship,
    to find the real grades that have been calculated."""
    num = int(input())
    for num in range(1, num):
        for i in range(2,num):
            if num % i != 0:
                print (num)
grade()
