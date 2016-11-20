"""this is a docstring"""
def perfection():
    """this is a docstring"""
    all_total = 0
    for j in range(1, int(input())):
        total = 0
        for i in range(1, j):
            if j % i == 0:
                total += i
            print(total)
        if total == j:
            all_total += total
    print(all_total)
    print("thats all")
perfection()
