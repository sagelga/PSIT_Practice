"""this is a docstring"""
def chocolate():
    """this is text"""
    size, big, small = int(input()), int(input()), int(input())
    if (big * 5) + small >= size:
        big_use = min(big, (size // 5))
        small_use = size - (big_use * 5)
        if small_use > small:
            return -1
    else:
        return -1
    return small_use
print(chocolate())