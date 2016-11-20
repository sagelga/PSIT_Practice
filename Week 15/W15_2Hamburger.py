"""This is a docstring"""
def hamburger(left, right):
    """This is a docstring"""
    print("|" * left + "*" * 2*(left+right) + "|" * right)
hamburger(int(input()), int(input()))
