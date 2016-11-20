"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    num = int(input())
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("No")
                break
            else:
                print("Yes")
    else:
        print("No")
major_branch()
