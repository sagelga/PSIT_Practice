"""This program will print out different types of string, depending on size."""
def percen():
    """This thing should work"""
    message = float(input())
    print("|" + "%.2f" %(message) + "|")
    print("|" + "+" + "%.2f" %(message) + "|")
    print("|" + "%10.2f" %(message) + "|")
    print("|" + "%-10.2f" %(message) + "|")
    print("|" + "%010.2f" %(message) + "|")
percen()
