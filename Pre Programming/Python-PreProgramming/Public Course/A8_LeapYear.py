"""This program will check either the year are leap year or not"""
def leapyear_calc():
    """This is the main fuction. It will do everything."""
    year = int(input()) - 543
    if year % 400 == 0:
        year += 543
        print("True")
    else:
        if year % 100 == 0:
            year += 543
            print("False")
        else:
            if year % 4 == 0:
                year += 543
                print("True")
            else:
                year += 543
                print("True")
leapyear_calc()
