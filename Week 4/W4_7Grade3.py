"""This program will count 1 to 100"""
def grading(divident):
    """This function will make a count and print out"""
    counter = 0
    for _ in range(divident):
        raw_score = float(input()) - 60
        while raw_score >= 0:
            counter += .5
            raw_score -= 5
    counter /= divident
    counter *= 100
    counter = int(counter)
    print("%.2f" %(counter / 100))
grading(int(input()))
