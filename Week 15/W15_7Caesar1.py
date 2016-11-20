"""This is a docstring"""
def ciphering(shift, text):
    """I am a function. I can jobs."""
    for i in text:
        listing, res = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", i
        if i.isalpha():
            res = listing[(listing.find((i.lower()))) + shift]
            if i.isupper():
                res = res.upper()
        print(res, end="")
ciphering(int(input()) % 26, input())
