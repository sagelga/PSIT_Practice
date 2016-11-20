"""This is text"""
import json
def cellular():
    """This is text"""
    length, total = int(input()), 0
    user = json.loads(input())
    user = sorted(user)
    while True:
        if len(user) == 0:
            break
        total += 1
        coverage = user[0] + (2 * length)
        for _ in range(len(user)):
            if user[0] <= coverage:
                user.remove(user[0])
            continue
    print(total)
cellular()