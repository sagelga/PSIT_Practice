"""Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number"""
def caller(limit):
    """This function will do something very coool"""
    if limit == 1:
        print("01")
        return
    for i in range(limit, 0, -1):
        print("%02d" %(i), end=" ")
    for i in range(1, limit):
        print("%02d" %(i+1), end=" ")
    print()
    for j in range(2):
        if j == 1:
            lines, minimum, do_a, do_b = 1, limit-1, 1, -1
        else:
            lines, minimum, do_a, do_b = limit, 0, -1, 1
        for _ in range(limit-1):
            lines, minimum= (lines + (1 * do_a)) , (minimum + (1 * do_b))
            for i in range(lines, limit+1):
                print("%02d" %(i), end=" ")
            for i in range(limit-1, minimum, -1):
                print("%02d" %(i), end=" ")
            for i in range(minimum+1, limit):
                print("%02d" %(i+1), end=" ")
            for i in range(limit-1, lines-1, -1):
                print("%02d" %(i), end=" ")
            print()

caller(int(input()))
