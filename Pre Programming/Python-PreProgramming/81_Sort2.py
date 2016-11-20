"""This program will input of 4 numbers. And they will filter out ascendingly"""
def ascending():
    """This will filter out the numbers from low to high, then print"""
    var_a = int(input())
    var_b = int(input())
    var_c = int(input())
    var_d = int(input())
    if var_a > var_b:
        var_a, var_b = var_b, var_a
    if var_b > var_c:
        var_b, var_c = var_c, var_b
    if var_c > var_d:
        var_c, var_d = var_d, var_c
    if var_a > var_b:
        var_a, var_b = var_b, var_a
    if var_b > var_c:
        var_b, var_c = var_c, var_b
    if var_c > var_d:
        var_c, var_d = var_d, var_c
    if var_a > var_b:
        var_a, var_b = var_b, var_a
    if var_b > var_c:
        var_b, var_c = var_c, var_b
    if var_c > var_d:
        var_c, var_d = var_d, var_c
    print("%d\n%d\n%d\n%d" %(var_a, var_b, var_c, var_d))
ascending()
