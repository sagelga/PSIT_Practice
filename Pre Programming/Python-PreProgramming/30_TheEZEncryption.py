"""This program will calculate and find the key, which is the answer"""
def codingin():
    """This thing will worked just fine"""
    keyis = int(input())
    charact = ord(input())
    print(charact+(keyis * 2 // 10 + 50 - charact))
codingin()
