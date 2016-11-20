"""This prorgam will print out new time"""
def calculate(align, margin, txt):
    """This program will calculate the new time with given second"""
    length, lft_ali, rgt_ali = (align - len(txt)), "", ""
    if margin == "left":
        lft_ali = " " * length
    if margin == "right":
        rgt_ali = " " * length
    if margin == "center":
        rgt_ali = " " * ((length // 2) + (length % 2))
        lft_ali = " " * (length // 2)
    print(rgt_ali + txt + lft_ali)
calculate(int(input()), input(), input())

