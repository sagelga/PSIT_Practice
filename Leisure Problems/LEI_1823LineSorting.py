"""this is function. I can do something"""
def sorting():
    """this is function"""
    listing = []
    for _ in range(int(input())):
        listing.append(input())
        listing.sort(key=len)
    for i in listing:
        print(i)
sorting()
