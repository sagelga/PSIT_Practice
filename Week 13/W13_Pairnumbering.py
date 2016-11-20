"""062: PairNumbering Problem"""
import json
def summation():
    """."""
    data1 = json.loads(input())
    data2 = json.loads(input())
    num = int(input())
    count = 0
    for i in data1:
        for k in data2:
            if i+k == num:
                count += 1
    print(count)
summation()