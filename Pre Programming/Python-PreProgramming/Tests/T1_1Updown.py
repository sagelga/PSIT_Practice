"""This program will reverse the word case. Upper to lower vice-versa"""
def switchcase():
    """This thing will revese the case of the word"""
    message = input()
    if message.islower == True:
        print(message.upper())
    if message.isupper == True:
        print(message.lower())
switchcase()
