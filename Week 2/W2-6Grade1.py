"""This program will test is the number excede 60"""
def grade_check():
    """This function will test the number excede 60. If yes, print YES"""
    number = float(input())
    if number >= 60:
        print("Pass")
    if number < 60:
        print("Fail")
grade_check()
