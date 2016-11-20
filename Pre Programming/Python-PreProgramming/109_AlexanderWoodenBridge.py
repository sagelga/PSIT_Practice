"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    distance = int(input())
    long_brick = int(input())
    short_brick = int(input())
    if distance <= ((long_brick * 4) + short_brick):
        long_brick_use = distance // 4
        short_brick_use = distance - (long_brick_use * 4)
        if long_brick_use >= long_brick or short_brick_use <= short_brick:
            print("Ionioi Hetairoi!!!")
            print("Large Wood :", int(long_brick_use))
            print("Small Wood :", int(short_brick_use))
        else:
            print("We failed, men.")
    else:
        print("We failed, men.")
major_branch()
