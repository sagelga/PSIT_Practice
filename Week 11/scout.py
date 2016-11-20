"""This is a docstring"""
def scout():
    """This is a docstring"""
    for _ in range(int(input())):
        test_spec = input().split()
        weight = input().split()
        weight = [int(i) for i in weight]
        weight = sorted(weight)
        total, count = 0, 0
        for i in range(min(int(test_spec[1]), len(weight))):
            if int(weight[i]) + total <= int(test_spec[2]):
                total += int(weight[i])
                count += 1
        print(count)

scout()
