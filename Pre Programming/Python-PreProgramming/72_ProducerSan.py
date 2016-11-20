"""This program will ask input > run code & algorithm > output"""
def major_branch():
    """This is the main fuction. It will do everything."""
    name = input()
    age = int(input())
    emotions = input()
    if (len(name) * 1.5) >= 10:
        points = 10
    else:
        points = len(name) * 1.5
    if age < 30:
        points += (30 - age) * .5
    if emotions == "Egao":
        points += 10
    else:
        if emotions == "Yes":
            points += 5
        else:
            if emotions != "No":
                points -= len(emotions)
    print("Name :", name)
    print("Score :", points)
    if points >= 15:
        print("Pass Project Cinderella")
    else:
        print("Not Pass")
major_branch()
