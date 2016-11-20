"""This program will hello the text"""
def caller():
    """This program will hello the text"""
    eng_txt = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    txt = input()
    if txt[0] in eng_txt:
        print("Hello " + txt + ".")
    else:
        print("สวัสดี " + txt)

caller()
