"""This program will arrange item in order in ascending or descending"""
def junction():
    """This will find out the input and sent the results to coorespond fuction"""
    (todo, number1, number2, number3) = (input(), float(input()), float(input()), float(input()))
    if number1 > number2:
        number1, number2 = number2, number1
    if number2 > number3:
        number2, number3 = number3, number2
    if number1 > number2:
        number1, number2 = number2, number1
    if number2 > number3:
        number2, number3 = number3, number2
    if todo != "Ascend":
        number1, number3 = number3, number1
    print("%.2f" %number1 + ", " + "%.2f" %number2 + ", " + "%.2f" %number3)
junction()
