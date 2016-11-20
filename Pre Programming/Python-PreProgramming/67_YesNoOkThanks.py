"""This program will find the way to complete this course"""
def major_branch():
    """This is the main fuction. It will do everything."""
    message = input()
    if message.isalpha:
        message = len(message)
        if message <= 3:
            print("Yes")
        else:
            if message >= 4 and message <= 10:
                print("No")
            else:
                if message > 10 and message <= 20:
                    print("Ok")
                else:
                    if message <= 100:
                        print("Thank You")
                    else:
                        print("OMFG To Many For Me GG")
major_branch()
