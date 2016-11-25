"""this is a docstring"""
def difference():
    """this is a docstring"""
    set_a, set_b, listing = int(input()), int(input()), []
    for _ in range(set_a):
        listing.append(int(input()))
    for _ in range(set_b):
        num = int(input())
        if num in listing:
            listing.remove(num)
    for i in listing:
        print(i, end=" ")
difference()
