"""05F: FibonacciRecursion Problem"""
def find_fibo(num):
    """find fibonacci sequence"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return find_fibo(num-1)+find_fibo(num-2)

print(find_fibo(int(input())))
