"""this is docstring"""
def counter(total):
    """this is docstring"""
    maximum, listing, trigger, count = int(input()), [], 1, 0
    for i in range(maximum):
        listing.append(int(input()))
        listing.sort()
    for i in range(1, total+1):
        if listing.count(i) >= (maximum / 2):
            print(i, listing.count(i))
            trigger = 0
            return
    if trigger:
        for i in range(1, total+1):
            if listing.count(i) > count:
                count = listing.count(i)
        print(0, count)
counter(int(input()))
