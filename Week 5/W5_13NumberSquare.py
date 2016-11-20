"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will print increment of each number
"""
def upper_half():
    """This function will do something very coool"""
    limit = int(input())
    if limit == 1:
        print("01")
        return
    lines = 1
    extras = limit
    total_indent = (2 * limit)-1
    print("01 " * total_indent)
    for _ in range(limit-2):
        indent = 0
        lines += 1
        for i in range(lines):
            print("%02d" %(i+1), end = " ")
            indent += 1
        for _ in range(total_indent - indent - lines):
            print("%02d" %lines, end = " ")
        for i in range(lines, 0, -1):
            print("%02d" %(i), end = " ")
        print()
        extras -= 2
    central(limit)
    lower_half(limit, total_indent)

def central(limit):
    for i in range(limit):
        print("%02d" %(i+1), end = " ")
    for i in range(limit, 1, -1):
        print("%02d" %(i-1), end = " ")
    print()

def lower_half(limit, total_indent):
    lines = limit
    extras = limit - 4
    for _ in range(limit - 1):
        indent = 0
        lines -= 1
        for i in range(lines):
            print("%02d" %(i+1), end = " ")
            indent += 1
        for _ in range(total_indent - indent - lines):
            print("%02d" %lines, end = " ")
        for i in range(lines, 0, -1):
            print("%02d" %(i), end = " ")
        print()
        extras += 2

upper_half()
