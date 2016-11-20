"""this is a docstring"""
def flattened():
    """this is a docstring"""
    good = [",", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    new = ""
    for i in input():
        if i in good:
            new += i
    new.split(",")
    print(new)
    new.sort(reverse="True")
flattened()
