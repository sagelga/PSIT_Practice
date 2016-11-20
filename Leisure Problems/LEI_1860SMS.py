"""this is text"""
def sms():
    """this is text"""
    list2 = "ABC"
    list3 = "DEF"
    list4 = "GHI"
    list5 = "JKL"
    list6 = "MNO"
    list7 = "PQRS"
    list8 = "TUV"
    list9 = "WXYZ"
    newlist = ""
    for i in range(int(input())):
        listing = int(input())
        if listing == 1:
            if newlist == "":
                continue
            newlist = newlist[0:i-1]
            continue
        if listing == 2:
            newlist += list2[(int(input()) + 2) % 3]
        if listing == 3:
            newlist += list3[(int(input()) + 2) % 3]
        if listing == 4:
            newlist += list4[(int(input()) + 2) % 3]
        if listing == 5:
            newlist += list5[(int(input()) + 2) % 3]
        if listing == 6:
            newlist += list6[(int(input()) + 2) % 3]
        if listing == 7:
            newlist += list7[(int(input()) + 3) % 4]
        if listing == 8:
            newlist += list8[(int(input()) + 2) % 3]
        if listing == 9:
            newlist += list9[(int(input()) + 3) % 4]
    print(newlist)
sms()
