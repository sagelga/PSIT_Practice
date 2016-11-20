"""
Pair Programming by Kunanon Srisuntiroj 59070022:
This program will calculate the long of the virus
"""
def long_find(virus, times):
    """This function will calculate the long of the virus"""
    for i in virus:
        if i == "o":
            times += 1
    print(times)
long_find(input().strip(), 0)
