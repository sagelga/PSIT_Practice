"""This program will find out the final wheel from the data given,
but stop when the criteria are not pass"""
def weightingstation():
    """The function will check is either legitable to find the final number"""
    average_weight = float(input())
    total_weight = average_weight * 4
    counter = 1
    wheel_1 = float(input())
    wheel_2 = float(input())
    wheel_3 = float(input())
    wheel_4 = float((total_weight - (wheel_1 + wheel_2 + wheel_3)))
    if total_weight >= 15000:
        print("Overweight")
        counter = 0
    bottom_half_average = average_weight * .5
    top_half_average = average_weight * 1.5
    if (wheel_1 > top_half_average) or (wheel_1 < bottom_half_average):
        if counter:
            print("Unbalance")
        counter = 0
    if (wheel_2 > top_half_average) or (wheel_2 < bottom_half_average):
        if counter:
            print("Unbalance")
        counter = 0
    if (wheel_3 > top_half_average) or (wheel_3 < bottom_half_average):
        if counter:
            print("Unbalance")
        counter = 0
    if (wheel_4 > top_half_average) or (wheel_4 < bottom_half_average):
        if counter:
            print("Unbalance")
        counter = 0
    if counter:
        print("Pass", "%.2f" %(wheel_4))
weightingstation()
