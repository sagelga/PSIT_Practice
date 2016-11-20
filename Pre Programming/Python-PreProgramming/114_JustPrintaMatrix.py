"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    length = int(input())
    width = int(input())
    len_counter = 0
    wid_counter = 0
    message = ""
    while wid_counter != width:
        while len_counter != length:
            news = input()
            news += message + " "
            len_counter += 1
        print("")
        wid_counter += 1
        len_counter = 0
        print(news)
        messenger = ""
major_branch()
