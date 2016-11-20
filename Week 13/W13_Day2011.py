"""find dey"""
def find(day, month):
    """'find day from the input"""
    day_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for i in range(month):
        day += day_month[i]
    day %= 7
    out = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    print(out[day])
find(int(input()), int(input()))