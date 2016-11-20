"""this is text"""
def almostmin():
    """this is text"""
    listing = []
    for _ in range(int(input())):
        text = int(input())
        if text not in listing:
            listing.append(text)
        listing.sort()
    if len(listing) > 1:
        print(listing[1])
    else:
        print("NONE")
almostmin()
