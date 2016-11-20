"""This program will reverse the word case. Upper to lower vice-versa"""
def checkers():
    """This thing will revese the case of the word"""
    message_a = input()
    message_b = input()
    coord_a = ord(message_a.upper()[0])
    coord_c = ord(message_b.upper()[0])
    coord_b = int(message_a[1])
    coord_d = int(message_b[1])
    differ = max(coord_a, coord_c) - min(coord_c, coord_a)
    difer = max(coord_b, coord_d) - min(coord_b, coord_d)
    if differ == difer:
        print("True")
    else:
        print("False")
checkers()
