"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    text = input().lower()
    raw_txt = text.split(",")
    message = []
    for i in raw_txt:
        number = text.count(i)
        message.append(number)
    print(max(text))
    positions = ((message).index((max(message))))
    print(text[positions])
major_branch()
