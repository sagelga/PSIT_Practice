"""This program will check either the project can be finished or not.
Second mission is to use minimum small brick."""
def builder():
    """Program will optimize the brick usage"""
    small_brick = int(input())
    large_brick = int(input())
    goal = int(input())
    large_use = goal // 5
    large_capacity = large_brick * 5
    small_use = goal - (large_brick * 5)
    if (small_brick + large_capacity < goal) or (goal - large_capacity != small_brick):
        print(-1)
    else:
        if large_brick >= large_use:
            print(goal // 5)
            print(goal % 5)
        else:
            print(large_brick)
            print(small_use)
builder()
