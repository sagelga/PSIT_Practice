"""Pair Programming Week 7 by K. Srisuntiroj ID0022
The program will only print out the text that are longer than 6 letters"""
def breaching(txt):
    """This function will print out the text that are longer than 6 letters"""
    runners = txt.count(" ") + 1
    for i in range(runners):
        if (runners - 1) == i:
            next_space = len(txt)
        else:
            next_space = txt.find(" ") + 1
        check_txt = txt[:next_space]
        counter = 0
        for j in check_txt:
            if j in available_txt:
                counter += 1
            if counter > 7:
                for k in check_txt:
                    if k in available_txt:
                        print(k, end="")
                break
        txt = txt[next_space:]

available_txt = "QWERTYUIOPASDFGHJKLZXCVBNM qwertyuiopasdfghjklzxcvbnm"
breaching(input())
