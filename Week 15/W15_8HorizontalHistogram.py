"""THis is a blank docstring"""
def alphabetcount(text, letter, upletter):
    """This is a dogstring"""
    for i in text:
        if (i.islower()) and (i not in letter):
            letter.append(i)
        elif (i.isupper()) and (i not in upletter):
            upletter.append(i)
    printer(letter, text)
    printer(upletter, text)

def printer(letter, text):
    """This is a dogstring"""
    letter.sort()
    for i in letter:
        print(i, ":", "", end="")
        for j in range(text.count(i)):
            if (j % 5 == 0) and j > 0:
                print("|-", end="")
            else:
                print("-", end="")
        print("")
alphabetcount(input(), [], [])
