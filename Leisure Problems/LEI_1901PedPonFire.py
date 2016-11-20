"""this is a docstring"""
def ped():
    """this is a docstring"""
    listing, count = [], 0
    for _ in range(int(input())):
        listing.append(int(input()))
    total = int(input())
    for i in range(len(listing)):
        for j in range(i+1, len(listing)):
            if listing[i] + listing[j] == total:
                count += 1
    print(int(count))
ped()
