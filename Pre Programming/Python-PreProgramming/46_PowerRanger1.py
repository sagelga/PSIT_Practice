""" Power ! ! ! """
def codingin():
    """Asking message and use word \\_(-*-)_/, dependence on length"""
    message = input()
    counter = len(message)
    counter = counter % 2
    print(("\\_(-*-)_/" * (counter + 1)) + message)
codingin()
