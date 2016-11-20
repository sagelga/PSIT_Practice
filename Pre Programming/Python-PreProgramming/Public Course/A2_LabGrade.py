"""This program will run wheaver the input is in range of 0-120 and change back to grades"""
def grade():
    """It is doing some nested if-else relationship,
    to find the real grades that have been calculated."""
    raw_grade = int(input())
    if 100 <= raw_grade <= 120:
        print("A")
    if 95 <= raw_grade < 100:
        print("B+")
    if 90 <= raw_grade < 95:
        print("B")
    if 85 <= raw_grade < 90:
        print("C+")
    if 80 <= raw_grade < 85:
        print("C")
    if 75 <= raw_grade < 80:
        print("D+")
    if 70 <= raw_grade < 75:
        print("D")
    if raw_grade < 70:
        print("F")
grade()
