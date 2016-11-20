"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will calculate total calories burned
"""
rdef triathelon(swim, cycle, runs):
    """This function will calculate calories burned"""
    counter = 0
    for _ in range(25600):
        counter += swim
    for _ in range(746):
        counter += cycle
    for _ in range(2122):
        counter += runs
    print("%.02f" %(counter))

for _ in range(int(input())):
    triathelon(float(input()), float(input()), float(input()))
