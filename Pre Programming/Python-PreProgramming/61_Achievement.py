"""
This program will output the achievements that have been compared with number
Part of the Preprogramming Course 2016
"""
def achievements():
    """Input will determine how many achiements received"""
    deaths = int(input())
    print("-----AchievementOfFail-----")
    if deaths >= 1:
        print("FirstTime of Fail")
    if deaths >= 10:
        print("King of Fail")
    if deaths >= 100:
        print("God of Fail")
    if deaths >= 1000:
        print("Omg r u kidding me")
achievements()
