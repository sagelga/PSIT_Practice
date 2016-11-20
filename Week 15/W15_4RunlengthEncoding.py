"""THis is a docstring"""
def encoder():
    """THis is a docstring"""
    text = input()
    current = text[0]
    count = 0
    for i in text:
        if i == current:
            count += 1
        if i != current:
            print(count, end="")
            print(current, end="")
            count = 0
            current = i
            count += 1
    print(count, end="")
    print(current, end="")
encoder()