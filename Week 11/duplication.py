"""This is a docstring"""
def duplication():
    """This is not empty"""
    list_a, list_b, count = [], [], True
    group_a, group_b = int(input()), int(input())
    for _ in range(group_a):
        list_a.append(input())
    for _ in range(group_b):
        list_b.append(input())
    list_a, list_b = set(list_a), set(list_b)
    intersec = list(list_a.intersection(list_b))
    intersec.sort(key=int, reverse=True)
    for i in intersec:
        print(i)
        count = False
    if count:
        print("Nope")

duplication()
