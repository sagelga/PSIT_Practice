"""This program will check either the year are leap year or not"""
def leapyear_calc():
    """This function will calculate the leap year based on given input"""
    year = int(input())
    if year % 400 == 0:
        print("Yes")
    elif year % 100 == 0:
        print("No")
    elif year % 4 == 0:
        print("Yes")
    else:
        print("No")
leapyear_calc()
