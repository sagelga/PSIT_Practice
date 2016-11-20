"""This program will ask input then, run the program, later then print out the results"""
def major_branch():
    """This is the main fuction. It will do everything."""
    message = list(input())
    message.sort(reverse=True)
    message_new = []
    for i in message:
        if message_new.count(i) == 0:
            message_new.append(i)
    print(message_new)
    answer = []
    i = 0
    for i in message_new:
        answer.append(message.count(i))
    answer.sort(reverse=True)
    print(answer)
major_branch()
