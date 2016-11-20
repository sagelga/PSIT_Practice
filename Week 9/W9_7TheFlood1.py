"""This program will calculate the attempt to keep the flood from getting through"""
def caller(text):
    """This function does it all"""
    count = 0
    text = text.split()
    for i in range(len(text)):
        text[i] = int(text[i])
    while 1:
        text.sort()
        for i in range(1, len(text)):
            if text[i] == 0 or text[0] == 0:
                return count
            else:
                text[i] = int(text[i]) - 1
        count += 1

print(caller(input()))
