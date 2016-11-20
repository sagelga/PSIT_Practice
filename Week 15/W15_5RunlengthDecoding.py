"""THis is a docstring"""
def decoder():
    """THis is a docstring"""
    number = ""
    text = input()
    for i in text:
        if i.isalpha():
            print(int(number) * i, end="")
            number = ""
        else:
            number += i
decoder()