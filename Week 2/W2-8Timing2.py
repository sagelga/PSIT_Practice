"""This program will calculate the day hour minuite second from the second given"""
def time_calculator():
    """This function will recieve input, run through calculations and given results"""
    raw_second = int(input())
    days = raw_second // 86400
    counter = 1
    if days >= 10000:
        print("ERR_:__:__:__")
        counter = 0
    if counter:
        hours = (raw_second % 86400) // 3600
        minutes = ((raw_second % 86400) % 3600) // 60
        second = ((raw_second % 86400) % 3600) % 60
        print("%04d" %(days)+":"+"%02d" %(hours) + ":" + "%02d" %(minutes) + ":" + "%02d" %(second))
time_calculator()
