"""This program will count the weight of the eligible chicken weight"""
def chickenweight():
    """This function will call out the other function to test the chicken weight"""
    count = 0
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    count += counter(int(input()))
    print(count)
def counter(weight):
    """This function will test the weight of the chicken, then return the results"""
    if weight >= 50 and weight <= 70:
        return 1
    if weight < 50 or weight > 70:
        return 0
chickenweight()
