"""this is a docstring"""
def backwards():
    """this is a docstring"""
    listing = []
    while True:
        text = input()
        if text == "NULL":
            for i in range(1, len(listing) + 1):
                print(listing[-i])
            break
        listing.append(text)
backwards()
