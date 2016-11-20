"""This do something"""
def caller():
    """This will do another thing"""
    line, trigger = input(), True
    line = line.replace(".", "")
    line = line.split()
    line = sorted(line)
    for i in line:
        counts = 0
        counts += i.count("A") + i.count("E") + i.count("I") + i.count("O") + i.count("U")
        counts += i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")
        if counts >= 2:
            print(i)
            trigger = False
    if trigger:
        print("Nope")

caller()
