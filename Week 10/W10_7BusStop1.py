"""this is a docstring"""
def bus_hub():
    max_cap, count = int(input()), 0
    for i in range(int(input())):
        line = input().split()
        line = [int(i) for i in line]
        station = line.pop(0)
        print("Testing at", station)
        for j in line:
            if line[j] < station
                
bus_hub()
