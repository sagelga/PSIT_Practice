"""Pair Programming by Kunanon S. 59070022
This program will calculate the answer, based on the numbers given"""
def catalan(ans):
    """This program will calculate the answer, based on the numbers given"""
    for i in range(ans, int(input())):
        ans = int((((4 * i)+2) / (i+2))* ans)
    print(ans)

catalan(1)
