"""This is docstring"""
def diamond():
    """This is docstring"""
    rows, column, total = int(input()), int(input()), []
    for i in range(column):
        total.append(0)
    for i in range(rows):
        listing = input().split()
        listing = [int(i) for i in listing]
        for i in range(column):
            total[i] += listing[i]
    print(max(total))

diamond()
