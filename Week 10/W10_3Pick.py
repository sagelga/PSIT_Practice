"""this is docstring"""
def pick():
    """this is docstring"""
    import json
    listing = json.loads(input())
    keys = input()
    if keys in listing:
        print("Yes")
        print(listing[keys])
    else:
        print("No")

pick()
