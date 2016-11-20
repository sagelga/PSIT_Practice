"""This prorgam will print out new time"""
def time_convert(sec, new_sec, new_min, new_hrs):
    """This prorgam will print out new time"""
    days = sec // (new_sec * new_min * new_hrs)
    sec -= (new_sec * new_min * new_hrs) * days
    hrs = sec // (new_sec * new_min)
    sec -= (new_sec * new_min) * hrs
    minuite = sec // new_sec
    sec -= new_sec * minuite
    print("%d" %hrs + ':' + "%d" %minuite + ':' + "%d" %sec)

time_convert(int(input()), int(input()), int(input()), int(input()))

