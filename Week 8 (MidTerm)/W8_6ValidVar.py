"""Pair Programming by Kunanon S. 59070022
This program will determine the variables that have been input"""
def text_validity(text):
    """This function of a single input as they are good or not"""
    if text[0] in numberline:
        return False
    for i in text:
        if (i not in numberline) and (i not in englishline):
            return False
    if text == "if" or text == "else" or text == "elif" or text == "while" or text == "for" \
        or text == "True" or text == "False" or text == "continue" or text == "break" \
        or text == "return" or text == "is" or text == "in" or text == "and" or text == "or" \
        or text == "from" or text == "as" or text == "pass" or text == "not" or text == "def" \
        or text == "None":
        return False
    return True

def calling():
    """This function calls another function x times"""
    for _ in range(int(input())):
        if text_validity(input()):
            print("Valid")
        else:
            print("Invalid")

numberline = "0123456789"
englishline = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_"
calling()
