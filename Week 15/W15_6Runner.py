"""Incomplete Code. Not yet ready to be sent"""
def gulico(distance, row, speed, time):
    """This is a docstring"""
    for i in range(int(input())):
        runner = input().split(" ")
        timer = (distance - (int(runner[1])) / int(runner[0]))
        print(timer)
        if (timer > time):
            time, speed, row = timer, int(runner[0]), i+1
        if timer == time and int(runner[0]) > speed:
            time, speed, row = timer, int(runner[0]), i+1

    print(row)
gulico(int(input()), 1, 0, 0)
