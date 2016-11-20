"""this is a docstring"""
def dignity():
    """this is a docstring"""
    while True:
        num = int(input())
        if num == 0:
            break
        while True:
            total = 0
            if num > 9:
                for i in str(num):
                    total += int(i)
                num = total
            else:
                print(num)
                break
dignity()
