"""Not finish work"""
def primary():
    """this is text"""
    count = 0
    upper = int(input())
    for i in range(1,upper+1):
        if (upper % i) != 0:
            print(i)
primary()