"""this is a docstring"""
def happy():
    """this is a docstring"""
    count = 0
    listing = input().split(",")
    for i in range(len(listing)):
        listing[i] = int(listing[i])
    for i in range(len(listing)):
        if listing[i] >= 80:
            count += 1
        elif listing[i] >= 20 and (listing[i] - listing[i-1]) >= 10:
            count += 1
    print(count)
happy()
