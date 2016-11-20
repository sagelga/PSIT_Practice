"""GCD"""
def function(num1, num2):
    """find GCD. of the number that inputed"""
    if num1 > num2:
        num3 = num1 - num2
        function(num2, num3)
    elif num1 < num2:
        num3 = num2 - num1
        function(num1, num3)
    else:
        if num1 == 1:
            print("YES")
        else:
            print("NO")
        print(num1)
function(int(input()), int(input()))