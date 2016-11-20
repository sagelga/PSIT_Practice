"""Pair Programming Week 7 by K. Srisuntiroj ID0022
The program will add number until being called end"""
def summation(num):
    """program add number"""
    while 1:
        txt = input()
        if txt == "Stop":
            print(num)
            break
        else:
            num += int(txt)

summation(0)
