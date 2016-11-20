"""This do something"""
def caller():
    """This will do another thing"""
    text, average, divider, newlist = [], 0, 0, []
    for _ in range(int(input())):
        text += input().split("\t")
    for i in range(1, len(text), 2):
        average += float("%.4f" %(float(text[i])))
        divider += 1
    average = average / divider
    for i in range(1, len(text), 2):
        if float(text[i]) <= average:
            newlist.append(float(text[i]))
        newlist.sort(key=int)
    print(text[(text.index(str(newlist[-1])))-1], end="\t")
    print(text[text.index(str(newlist[-1]))])

caller()

