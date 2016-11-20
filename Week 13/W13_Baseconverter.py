"""this is a blank docstring"""
def conv(num, num2, lett="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """this is a blank docstring"""
    return ((num==0) and lett[0]) or (conv(num//num2, num2, lett).lstrip(lett[0]) + lett[num%num2])
print(conv(int(input()), int(input())))