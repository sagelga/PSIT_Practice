"""Pair Programming Week 7 by K. Srisuntiroj ID0022
This program will calculate the distance travelled by projectile throw"""
import math
def projectile(angle, speed):
    """This will calculate the distance travelled by projectile throw"""
    if 0 <= angle <= 90:
        projectile = (((speed ** 2) * float("%.8f" %(math.sin(angle/360*2*math.pi*2))))/9.81)
        print("%.1f"%(projectile))
projectile(int(input()), int(input()))
