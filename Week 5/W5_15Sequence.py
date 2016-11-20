"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def calculations(max_number, maximus):
    """This function will do something very coool"""
    for _ in range(int(input())):
        number, count, value = int(input()), 1, number
        while value > 1:
            count += 1
            if value % 2 == 0:
                value /= 2
            else:
                value = (value * 3) + 1
        if count > maximus:
            maximus, max_number = count, number
    print(maximus, max_number)

calculations(0, 0)
