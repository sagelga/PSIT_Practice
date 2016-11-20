"""This thing do something"""
def caller():
    """This thing do another thing"""
    count, num, text = 0, int(input()), []
    for _ in range(num):
        raw_text = int(input())
        if raw_text != count:
            text.append(raw_text)
            count = raw_text
            text = sorted(text)
    if len(text) > 1:
        print(text[1])
    else:
        print("NONE")
caller()
