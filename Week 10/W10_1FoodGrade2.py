"""Input"""
def chicken():
    """Input"""
    total, count = 0, 0
    weight = int(input())
    grams = input().split()
    grams = [int(x) for x in grams]
    grams.sort()
    for i in grams:
        if int(i) + total <= weight:
            total += int(i)
            count += 1
    print(count)

chicken()
