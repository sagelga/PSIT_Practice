"""This program will print out different types of string, depending on size."""
def percen():
    """This thing should work"""
    message = input()
    print("|" + message + "|")
    print("|+" + message + "|")
    print("|" + "%10s" %(message) + "|")
    print("|" + "%-10s" %(message) + "|")
    print("|" + "%.5d" %(int(message)) + "|")
percen()
