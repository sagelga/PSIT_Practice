"""This program will print out different types of string, depending on size."""
def percen():
    """This should work"""
    message = input()
    print("|" + message + "|")
    print("|" + "%10s" %(message) + "|")
    print("|" + "%-10s" %(message) + "|")
    print("|" + "%.1s" %(message), "%.3s" %(message), "%.5s" %(message) + "|")
percen()
