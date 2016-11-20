"""this is docstring"""
def main():
    """this is docstring"""
    import json
    dic, filters, newlist, count = json.loads(input()), int(input()), [], 0
    for i in dic:
        numbers = dic[i]
        if numbers >= filters:
            newlist.append(i)
            count = 1
    newlist.sort()
    if count:
        for i in newlist:
            print(i, end="\t")
            print("%.2f" %dic[i])
    else:
        print("Nope")

main()
