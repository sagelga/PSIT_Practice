"""This program will convert between 12 hours timer into 24 hours timer."""
def major_branch():
    """This is the main fuction. It will do everything."""
    hours = int(input())
    minit = int(input())
    meridean = input()
    if hours == 12:
        if meridean == "AM":
            hours = 0
        elif meridean == "PM":
            hours = 12
    else:
        if meridean == "PM":
            hours += 12
    print("24 Hours time is", "%02d" %hours, ":", "%02d" %minit)
major_branch()
