"""This program will figuring out the other luggage weight by given input"""
def weightadjusts():
    """The function will adjust the average weight first, results in calculatable number"""
    average_kg = float(input()) * 2
    luggage_kg = float(input())
    print(average_kg - luggage_kg)
weightadjusts()
