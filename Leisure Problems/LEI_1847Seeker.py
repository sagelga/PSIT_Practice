"""this is a docstring"""
def seeking():
    """this is a docstring"""
    num, total = "", 0
    for i in input():
        if i.isdigit():
            num += i
        elif num != "":
            total += int(num)
            num = ""
    if num != "":
        total += int(num)
    print(total)
seeking()
