"""Pair Programming Week 7 by K. Srisuntiroj ID0022
The program will calculate the distance travelled of a HDD"""
def cylinder(time):
    """This will calculate the distance travelled of a HDD"""
    circumference = 2 * 3.14 * (2.5*2.54)
    surround = 15000 / 60
    print("%.02f" %(time * circumference * surround))
cylinder(int(input()))
