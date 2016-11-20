"""This program will ask input then, run the program, later then print out the results"""
def integer_calc():
    """This is the main fuction. It will do everything."""
    message = input()
    total = 0
    counter = 0
    while message.isdigit():
        total += int(message)
        counter += 1
        message = input()
    if not message.isdigit() and counter == 0:
        print("Python is very Ez")
    else:
        print("Sum of number is", total)
        print("Average is :", "%.2f" %(total / counter))
integer_calc()
