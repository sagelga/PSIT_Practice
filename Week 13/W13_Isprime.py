"""This is a blank page"""
def prime(number):
    """ABCDE"""
    if number <= 1:
        print("NO")
    for i in range(2, number):
        if number % i == 0:
            print("NO")
            return
    print("YES")
prime(int(input()))